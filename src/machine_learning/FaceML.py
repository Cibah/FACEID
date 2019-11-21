import os
from datetime import datetime
import lib.face_recognition.face_recognition as face_recognition
from src.config.Configurator import Configurator
from src.incidents.Mail import sendMail
from src.log.Logger import logger

# Load the jpg files into numpy arrays
# from lib.face_recognition.docs.conf import Mock
class FaceML:
    known_faces = []
    filelist = []
    path = ""
    time1 = datetime.now()

    def __init__(self):
        self.path = Configurator.get("data", "data_path_known_faces")
        self.load_known_faces()

    def load_known_faces(self):
        self.known_faces = []
        self.filelist = []
        time1 = datetime.now()
        if not os.path.exists(self.path):
            logger.error("Path not found_ " + self.path)
        logger.debug("Loading known faces")
        for face in os.listdir(self.path):
            logger.debug("Loading face " + face)
            if face.endswith(".jpg"):
                face_image = face_recognition.load_image_file(self.path + face)
                self.filelist.append(self.path + face)
                try:
                    encodings = face_recognition.face_encodings(face_image)
                    for face_encode in encodings:
                        self.known_faces.append(face_encode)
                except IndexError:
                    logger.error("No faces found in " + self.path + face)
                    # sendMail("No Face found in file", "self.path + face")
                except IOError:
                    logger.error("Cant open the face file " + self.path + face)
                    #sendMail("No Face found in file", "self.path + face")
        logger.debug("Loaded all " + str(len(self.known_faces)) + " faces in " + str(
            datetime.now() - time1) + " seconds")

    def check_face(self, image):
        unknown_face_encoding = []
        time1 = datetime.now()
        logger.debug("Loading unknown face")
        found = False
        try:
            unknown_image = face_recognition.load_image_file(image)
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            logger.error("No faces found in " + self.path + image)
            return found
        except IOError:
            logger.error("Cant open the unkown face file")
            return found
        logger.debug("Comparing the known faces with the unkown picture")
        results = face_recognition.compare_faces(self.known_faces, unknown_face_encoding)
        index = 0
        for result in results:
            if result:
                found = result
                print("Face found in : " + self.filelist[index])
            index += 1
        logger.debug("Processed Faces in " + str(datetime.now() - time1) + " seconds")
        logger.debug("Found known Face? : " + str(found))
        return found

# ml = FaceML(Configurator.get("data", "data_path_known_faces"))
# ml.check_face("../../img/unknown.jpg")
