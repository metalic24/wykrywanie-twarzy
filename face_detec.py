

import cv2
import face_recognition
from PIL import Image
import numpy as np


def camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()


    while True:

        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        img = cv2.imread("C:/Users/Mati/Pictures/myszka.png",-1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        for top, right, bottom, left in face_locations:

            a=(right-left)
            b=(bottom-top)
            img =  cv2.resize(img, (a, b))

            #usunięcie kanału alpha


            alpha_img = img[:, :, 3] / 255.0
            alpha_frame = 1.0 - alpha_img
            for c in range(0, 3):
                frame[top:bottom, left:right, c] = (alpha_img * img[:, :, c] +
                                                    alpha_frame * frame[top:bottom, left:right, c])

        cv2.imshow('Video', frame)


        # 'q' zamyka kamerę
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()


def zdjecie(path):


    image = cv2.imread(path)
    face_locations = face_recognition.face_locations(image)
    img = cv2.imread("C:/Users/Mati/Pictures/myszka.png",-1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    for top, right, bottom, left in face_locations:
        # cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        img = cv2.resize(img, ((right - left), (bottom - top)))


        a = (right - left)
        b = (bottom - top)

        alpha_img = img[:, :, 3] / 255.0
        alpha_image = 1.0 - alpha_img

        for c in range(0, 3):
                    image[top:bottom, left:right, c] = (alpha_img * img[:, :, c] +
                                                   alpha_image * image[top:bottom, left:right, c])


    return image





