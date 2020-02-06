from src.log.Logger import logger
from src.config.Configurator import Configurator as config
from src.incidents.Mail import sendMail
import requests


def openDoor():
    # open the door
    logger.debug("Opening the door")
    payload = {"command": "OFF"}
    try:
        r = requests.post(config.get("danalock", "openhab_lock_item"), 'OFF')
        logger.debug(str(r))
    except:
        logger.error("Danalock not available")
        sendMail("Danalock not available!: " + str(config.get("danalock", "openhab_lock_item")))


def lockDoor():
    logger.debug("Lock the door")
    try:
        r = requests.post(config.get("danalock", "openhab_lock_item"), 'ON')
        logger.debug(str(r))
    except:
        logger.error("Danalock not available")
        sendMail("Danalock not available!: " + str(config.get("danalock", "openhab_lock_item")))
