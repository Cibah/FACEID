from src.data.FaceML import *
from src.klingel.Klingel import *
from src.log.Logger import logger

user = "ggyzbm0001"
password = "yolutgwrvu"
url = "http://192.168.0.61"
path_to_known_faces = "../../img/known/"
version = "0.0.1"


def main():
    # Login for Events
    logger.debug("FaceID by HFU v")

    # init
    ml = FaceML(path_to_known_faces)

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


if __name__ == '__main__':
    main()
