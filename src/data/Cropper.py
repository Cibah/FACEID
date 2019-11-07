from PIL import Image
import face_recognition
import lib.face_recognition.face_recognition as face_recognition


def crop(image, file):
    image = face_recognition.load_image_file(image)
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    face_locations = face_recognition.face_locations(image)
    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        top = int(top * 0.7)
        left = int(left * 0.8)
        bottom = int(bottom * 1.1)
        right = int(right * 1.1)
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                    right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
        # pil_image.save(file)


crop("../../img/toCrop/artur.jpg")
