from PIL import Image
import face_recognition as face_recognition
from src.log.Logger import logger
import cv2


def upscale(image, scale):
    height, width = image.shape[:2]
    return cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_LINEAR)


def crop(image, file):
    result = False
    img = upscale(image)
    image = face_recognition.load_image_file(img)
    # the cnn net takes too much time and breaks with big images
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    face_locations = face_recognition.face_locations(img)
    logger.debug("Cropper found {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        result = True
        top, right, bottom, left = face_location
        top = int(top * 0.7)
        left = int(left * 0.8)
        bottom = int(bottom * 1.1)
        right = int(right * 1.1)

        face_image = img[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        # pil_image.show()
        pil_image.save(file)
    return result
# Usage
# crop("../../img/toCrop/artur.jpg")
