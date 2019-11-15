from src.klingel.Klingel import *

from src.config import Configurator
from src.incidents.Mail import sendMail
from src.log.Logger import logger
from src.machine_learning.FaceML import FaceML

user = "ggyzbm0001"
password = "yolutgwrvu"
url = "http://192.168.0.61"
version = "0.0.1"
failed_access = 0

def main():
    # Login for Events
    logger.debug("FaceID by HFU v")

    # init
    ml = FaceML(Configurator.get("data", "data_path_known_faces"))

    # TODO (philipp): open udp port and wait for event in while loop
    # after event: take photo and save somewhere?
    # check the face via:
    person_known = ml.check_face("../../img/unknown.jpg")
    if person_known:
        # open door
        logger.debug("Open the door")
    else:
        # do not open door
        logger.debug("No access")
        if (failed_access > Configurator.get("other", "max_num_of_failed_access")):
            sendMail("5 failed Access", "../../img/unknown.jpg")



if __name__ == '__main__':
    main()
