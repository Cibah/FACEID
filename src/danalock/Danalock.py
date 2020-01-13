from src.log.Logger import logger
import urllib.request
from src.config.Configurator import Configurator as config
from src.incidents.Mail import sendMail
import requests

def openDoor():
    # open the door
    logger.debug("Opening the door")
    payload = {"command": "OFF"}
    try:
        r = requests.post(config.get("danalock", "openhab_lock_item"), 'OFF')
    except:
        logger.error("Danalock not available")
        sendMail("Danalock not available!: " + str(config.get("danalock", "openhab_lock_item")))
    # urllib.request.URLopener().open(config.get("danalock", "openhab_unlock_url"))


def lockDoor():
    logger.debug("Lock the door")
    try:
        r = requests.post(config.get("danalock", "openhab_lock_item"), 'ON')
    except:
        logger.error("Danalock not available")
        sendMail("Danalock not available!: " + str(config.get("danalock", "openhab_lock_item")))
    #urllib.request.URLopener().open(config.get("danalock", "openhab_lock_url"))
