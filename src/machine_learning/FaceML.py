import os
from datetime import datetime
import face_recognition as face_recognition
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
        config = Configurator.get("data", "data_path_known_faces")
        final = config
        # logger.warn(final)
        self.path = final
        self.load_known_faces()

    def load_known_faces(self):
        self.known_faces = []
        self.filelist = []
        time1 = datetime.now()
        if not os.path.exists(self.path):
            logger.error("Path not found_ " + self.path)
        logger.info("Loading known faces")
        for face in os.listdir(self.path):
            logger.debug("Loading face " + face)
            if face.endswith(".jpg"):
                face_image = face_recognition.load_image_file(self.path + face)
                logger.debug("Checking File for faces: " + self.path + face)
                self.filelist.append(self.path + face)
                try:
                    encodings = face_recognition.face_encodings(face_image)
                    for face_encode in encodings:
                        self.known_faces.append(face_encode)
                except IndexError:
                    logger.error("No faces found in " + face)
                    # sendMail("No Face found in file", "self.path + face")
                except IOError:
                    logger.error("Cant open the face file " + face)
                    # sendMail("No Face found in file", "self.path + face")
        logger.info("Loaded " + str(len(self.known_faces)) + " faces in " + str(
            datetime.now() - time1) + " seconds")

    def load_new_face(self, image):
        time1 = datetime.now()
        logger.info("Loading the new face")
        face_image = face_recognition.load_image_file(image)
        try:
            encodings = face_recognition.face_encodings(face_image)
            for face_encode in encodings:
                self.known_faces.append(face_encode)
            self.filelist.append(image)
        except IndexError:
            logger.error("No faces found in " + image)
            # sendMail("No Face found in file", "self.path + face")
        except IOError:
            logger.error("Cant open the face file " + image)
            # sendMail("No Face found in file", "self.path + face")
        logger.info("Loaded all " + str(len(self.known_faces)) + " faces in " + str(
            datetime.now() - time1) + " seconds")

    def check_face(self, image):
        unknown_face_encoding = []
        time1 = datetime.now()
        logger.info("Checking unknown face")
        logger.warn(image)
        faces = []
        try:
            unknown_image = face_recognition.load_image_file(image)
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            logger.error("No faces found in " + self.path + image)
            return faces
        except IOError:
            logger.error("Cant open the unkown face file")
            return faces
        logger.debug("Comparing the known faces with the unkown picture")
        results = face_recognition.compare_faces(self.known_faces, unknown_face_encoding)
        index = 0
        for result in results:
            if result:
                logger.info("Face found in : " + self.filelist[index])
                faces.append(self.filelist[index])
            index += 1
        logger.debug("Processed Faces in " + str(datetime.now() - time1) + " seconds")
        logger.debug("Found known Face? : " + str((len(faces) != 0)))
        return faces

# ml = FaceML(Configurator.get("data", "data_path_known_faces"))
# ml.check_face("../../img/unknown.jpg")
