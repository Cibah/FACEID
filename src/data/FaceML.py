import face_recognition
import os
# Load the jpg files into numpy arrays
from lib.face_recognition.docs.conf import Mock

known_faces = []
path = "../../img/known/"
for face in os.listdir(path):
    if face.endswith(".jpg"):
        print("Exists? " + path+face)
        print(os._exists(path+face))
        face_image = face_recognition.load_image_file(path+face)
        try:
            face_encoding = face_recognition.face_encodings(face_image)[0]
            known_faces.append(face_encoding)
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()
# unknown_image = face_recognition.load_image_file("unknown.jpeg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.

try:
    unknown_image = face_recognition.load_image_file("../../img/unknown.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()


# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Maik? {}".format(results[0]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
