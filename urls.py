from aiohttp import web
from crud import create_device


def setup_routes(app):
    app.router.add_post('/devices', create_device)
