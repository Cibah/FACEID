from src.data.FaceML import *
from src.klingel.Klingel import *

# import face_recognition

user = "ggyzbm0001"
password = "yolutgwrvu"
url = "http://192.168.0.61"
path_to_known_faces = "../../img/known/"


def main():
    # Login for Events
    print("FaceID by HFU")
    # maybe in its own thread?
    # login_and_wait_for_event()
    ml = FaceML(path_to_known_faces)
    ml.check_face("../../img/unknown.jpg")
    ml.check_face("../../img/unknown.jpg")
    ml.check_face("../../img/unknown.jpg")
    ml.check_face("../../img/unknown.jpg")


if __name__ == '__main__':
    main()
