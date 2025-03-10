from aiohttp import web
from crud import (create_device,
                  get_devices,
                  get_device,
                  update_device,
                  delete_device,
                  create_location,
                  create_user)


def setup_routes(app):
    app.router.add_post("/devices", create_device)
    app.router.add_get("/devices", get_devices)
    app.router.add_get("/devices/{id}", get_device)
    app.router.add_route("PUT", "/devices/{id}", update_device)
    app.router.add_delete("/devices/{id}", delete_device)
    app.router.add_post("/locations", create_location)
    app.router.add_post("/users", create_user)
