from models import *
from playhouse.shortcuts import model_to_dict
from aiohttp import web


async def create_device(request):
    data = await request.json()
    device = Device.create(
        name=data['name'],
        type=data['type'],
        login=data['login'],
        password=data['password'],
        location=data['location_id'],
        api_user=data['api_user_id']
    )
    return web.json_response(model_to_dict(device))
