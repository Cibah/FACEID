from src.log.Logger import logger
import urllib.request
from src.config.Configurator import Configurator as config
import requests

def openDoor():
    # open the door
    logger.debug("Opening the door")
    payload = {"command" :"OFF"}
    r = requests.post(config.get("danalock", "openhab_lock_item"), 'OFF')
    #urllib.request.URLopener().open(config.get("danalock", "openhab_unlock_url"))


def lockDoor():
    logger.debug("Lock the door")
    r = requests.post(config.get("danalock", "openhab_lock_item"), 'ON')
    #urllib.request.URLopener().open(config.get("danalock", "openhab_lock_url"))
