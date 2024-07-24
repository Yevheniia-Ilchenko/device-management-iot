from aiohttp import web
from crud import create_device, get_devices, get_device, update_device


def setup_routes(app):
    app.router.add_post("/devices", create_device)
    app.router.add_get("/devices", get_devices)
    app.router.add_get("/devices/{id}", get_device)
    app.router.add_update("/devices/{id}", update_device)

