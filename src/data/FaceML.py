import os
from datetime import datetime

import lib.face_recognition.face_recognition as face_recognition


# Load the jpg files into numpy arrays
# from lib.face_recognition.docs.conf import Mock
class FaceML:
    known_faces = []
    path = ""
    time1 = datetime.now()

    def __init__(self, path):
        self.path = path
        self.load_known_faces()

    def load_known_faces(self):
        time1 = datetime.now()
        if not os.path.exists(self.path):
            print("Path not found: " + self.path)
            exit(-1)
        print("Loading all known faces ...")
        for face in os.listdir(self.path):
            print("Loading face: " + face)
            if face.endswith(".jpg"):
                face_image = face_recognition.load_image_file(self.path + face)
                try:
                    face_encoding = face_recognition.face_encodings(face_image)[0]
                    self.known_faces.append(face_encoding)
                except IndexError:
                    print(
                        "I wasn't able to locate any faces in at least one of the images. Check the image files. "
                        "Aborting...")
                    quit()
        print("Loaded all known faces: " + str(len(self.known_faces)) + " in: " + str(
            datetime.now() - time1) + " seconds")

    def check_face(self, face):
        unknown_face_encoding = []
        time1 = datetime.now()
        print("Loading unknown Face")
        found = False
        try:
            unknown_image = face_recognition.load_image_file(face)
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
        except IOError:
            print("Cant open the file")
            quit()
        print("Comparing all known Faces with the unknown")
        results = face_recognition.compare_faces(self.known_faces, unknown_face_encoding)
        for result in results:
            if result:
                found = result
        print("Found the face? " + str(found) + " in: " + str(datetime.now() - time1) + " seconds")
        return found
