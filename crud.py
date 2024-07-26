from models import *
from playhouse.shortcuts import model_to_dict
from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def create_device(request):
    logger.info("Create_device request")
    data = await request.json()
    required_keys = ["name", "type", "login", "password", "location_id", "api_user_id"]

    for key in required_keys:
        if key not in data:
            logger.warning(f"Missing key: {key} in request data")
            return web.json_response({"error": f"Missing key: {key}"}, status=400)
    try:
        device = Device.create(
            name=data["name"],
            type=data["type"],
            login=data["login"],
            password=data["password"],
            location=data["location_id"],
            api_user=data["api_user_id"],
        )
        logger.info(f"Created: {model_to_dict(device)}")
        return web.json_response(model_to_dict(device))
    except Exception as e:
        logger.error(f"Error creating device: {e}")
        return web.json_response({"error": "Failed to create device"}, status=500)


async def get_devices(request):
    logger.info("get_devices request")
    devices = Device.select()
    devices_list = []
    for device in devices:
        devices_list.append(model_to_dict(device))
    logger.info(f"Retrieved devices: {devices_list}")
    return web.json_response(devices_list)


async def get_device(request):
    try:
        device_id = int(request.match_info["id"])
    except ValueError:
        logger.warning("Invalid device ID")
        return web.json_response({"error": "Invalid device ID"}, status=400)

    device = Device.get_or_none(Device.id == device_id)
    if device:
        logger.info(f"Device found: {model_to_dict(device)}")
        return web.json_response(model_to_dict(device))
    else:
        logger.warning("Device not found")
        return web.json_response({"error": "Device not found"}, status=404)


async def update_device(request):
    device_id = request.match_info["id"]
    data = await request.json()
    try:
        query = Device.update(**data).where(Device.id == device_id)
        if query.execute():
            device = Device.get_by_id(device_id)
            logger.info(f"Device updated: {model_to_dict(device)}")
            return web.json_response(model_to_dict(device))
        else:
            logger.warning("Device not found")
            return web.json_response({"error": "Device not found"}, status=404)
    except Exception as e:
        logger.error(f"Error updating device: {e}")
        return web.json_response({"error": "Failed to update device"}, status=500)


async def delete_device(request):
    device_id = request.match_info["id"]
    try:
        query = Device.delete().where(Device.id == device_id)
        if query.execute():
            logger.info(f"Device deleted: {device_id}")
            return web.json_response({"message": "Device deleted"})
        else:
            logger.warning("Device not found")
            return web.json_response({"error": "Device not found"}, status=404)
    except Exception as e:
        logger.error(f"Error deleting device: {e}")
        return web.json_response({"error": "Failed to delete device"}, status=500)


async def create_location(request):
    logger.info("create_location request")
    data = await request.json()
    try:
        location = Location.create(name=data["name"])
        logger.info(f"Location created: {model_to_dict(location)}")
        return web.json_response(model_to_dict(location))
    except Exception as e:
        logger.error(f"Error creating location: {e}")
        return web.json_response({"error": "Failed to create location"}, status=500)


async def create_user(request):
    logger.info("create_user request")
    data = await request.json()
    try:
        user = ApiUser.create(
            name=data["name"],
            email=data["email"],
            password=data["password"],
        )
        logger.info(f"User created: {model_to_dict(user)}")
        return web.json_response(model_to_dict(user))
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return web.json_response({"error": "Failed to create user"}, status=500)
