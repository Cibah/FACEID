import os
from datetime import datetime
import lib.face_recognition.face_recognition as face_recognition
from src.log.Logger import logger


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
            logger.error("Path not found_ " + self.path)
        logger.debug("Loading known faces")
        for face in os.listdir(self.path):
            logger.debug("Loading face " + face)
            if face.endswith(".jpg"):
                face_image = face_recognition.load_image_file(self.path + face)
                try:
                    face_encoding = face_recognition.face_encodings(face_image)[0]
                    self.known_faces.append(face_encoding)
                except IndexError:
                    logger.error("No faces found in " + self.path + face)
                except IOError:
                    logger.error("Cant open the face file " + self.path + face)
        logger.debug("Loaded all " + str(len(self.known_faces)) + " faces in " + str(
            datetime.now() - time1) + " seconds")

    def check_face(self, face):
        unknown_face_encoding = []
        time1 = datetime.now()
        logger.debug("Loading unknown face")
        found = False
        try:
            unknown_image = face_recognition.load_image_file(face)
            # TODO (artur): How to cache the image?
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            logger.error("No faces found in " + self.path + face)
            return found
        except IOError:
            logger.error("Cant open the unkown face file")
            return found
        logger.debug("Comparing the known faces with the unkown picture")
        results = face_recognition.compare_faces(self.known_faces, unknown_face_encoding)
        for result in results:
            if result:
                found = result
        logger.debug("Processed Faces in " + str(datetime.now() - time1) + " seconds")
        logger.debug("Found known Face? : " + str(found))
        return found
