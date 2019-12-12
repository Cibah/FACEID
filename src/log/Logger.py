import logging
from src.config.Configurator import Configurator as config

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
level = logging.getLevelName(config.get("general", "debug_level_2"))
logger.setLevel(level)
# TODO(artur): logger.log(msg) not working!
