from models import *
from playhouse.shortcuts import model_to_dict
from aiohttp import web


async def create_device(request):
    data = await request.json()
    device = Device.create(
        name=data["name"],
        type=data["type"],
        login=data["login"],
        password=data["password"],
        location=data["location_id"],
        api_user=data["api_user_id"],
    )
    return web.json_response(model_to_dict(device))


async def get_devices(request):
    devices = Device.select()
    devices_list = []
    for device in devices:
        devices_list.append(model_to_dict(device))
    return web.json_response(devices_list)


async def get_device(request):
    try:
        device_id = int(request.match_info["id"])
    except ValueError:
        return web.json_response({"error": "Invalid device ID"}, status=400)

    device = Device.get_or_none(Device.id == device_id)
    if device:
        return web.json_response(model_to_dict(device))
    else:
        return web.json_response({"error": "Device not found"}, status=404)


async def update_device(request):
    device_id = request.match_info["id"]
    data = await request.json()
    query = Device.update(**data).where(Device.id == device_id)
    if query.execute():
        device = Device.get_by_id(device_id)
        return web.json_response(model_to_dict(device))
    else:
        return web.json_response({"error": "Device not found"}, status=404)


async def delete_device(request):
    device_id = request.match_info["id"]
    query = Device.delete().where(Device.id == device_id)
    if query.execute():
        return web.json_response({"message": "Device deleted"})
    else:
        return web.json_response({"error": "Device not found"}, status=404)
