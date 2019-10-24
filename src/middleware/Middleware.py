from src.klingel.Klingel import *
import face_recognition

user = "ggyzbm0001"
password = "yolutgwrvu"
url = "http://192.168.0.61"
path_to_known_faces="../../img/"

def main():
    # Login for Events
    print("FaceID by HFU")
    # maybe in its own thread?
    login_and_wait_for_event()


def check_Face(image):
    print("Event was fired: Button pushed: Someone wants to come in")
    known_image = face_recognition.load_image_file("../../img/maik.jpg")
    unkown_image = face_recognition.load_image_file("../../img/unknown.jpg")
    try:
        known_face_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_face_encoding = face_recognition.load_image_file(unkown_image)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()
    known_faces = [
        known_face_encoding
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print("Is this person known? ".format(results[0]))


if __name__ == '__main__':
    main()
