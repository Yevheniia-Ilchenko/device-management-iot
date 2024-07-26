import json
import pytest
from aiohttp import web
from models import db, Device, Location, ApiUser
from crud import create_device, get_devices, get_device, update_device, delete_device, create_location, create_user

pytestmark = pytest.mark.asyncio


@pytest.fixture
def app():
    app = web.Application()
    app.router.add_post('/devices', create_device)
    app.router.add_get('/devices', get_devices)
    app.router.add_get('/devices/{id}', get_device)
    app.router.add_patch('/devices/{id}', update_device)
    app.router.add_delete('/devices/{id}', delete_device)
    app.router.add_post('/locations', create_location)
    app.router.add_post('/users', create_user)
    return app


@pytest.fixture
async def client(aiohttp_client, app):
    test_client = await aiohttp_client(app)

    yield test_client


@pytest.fixture
async def setup_data(client):
    db.connect(reuse_if_open=True)
    db.drop_tables([ApiUser, Location, Device])
    db.create_tables([ApiUser, Location, Device])

    # Логування для перевірки очищення таблиць
    print("Tables dropped and recreated")
    print("ApiUser count after setup:", ApiUser.select().count())
    print("Location count after setup:", Location.select().count())
    print("Device count after setup:", Device.select().count())

    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password"
    }
    await client.post('/users', json=user_data)
    user = ApiUser.get(ApiUser.email == "test@example.com")

    location_data = {
        "name": "Test Location"
    }
    await client.post('/locations', json=location_data)
    location = Location.get(Location.name == "Test Location")

    device_data = {
        "name": "Test Device",
        "type": "Type A",
        "login": "testlogin",
        "password": "testpassword",
        "location_id": location.id,
        "api_user_id": user.id
    }

    # Логування для перевірки наповнення таблиць
    print("ApiUser count after data setup:", ApiUser.select().count())
    print("Location count after data setup:", Location.select().count())
    print("Device count after data setup:", Device.select().count())

    db.close()

    return user, location, device_data


@pytest.mark.asyncio
async def test_create_device(client, setup_data):
    user, location, device_data = setup_data

    # Test creating a device
    resp = await client.post('/devices', json=device_data)
    assert resp.status == 200
    data = await resp.json()
    assert data["name"] == "Test Device"
    assert data["type"] == "Type A"
