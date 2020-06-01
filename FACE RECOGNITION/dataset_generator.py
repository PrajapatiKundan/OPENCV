import cv2
import numpy as np

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_frontalface_default.xml")


def generate_dataset(img, id, img_id):
    cv2.imwrite("data1/user." + str(id) + "." + str(img_id) + ".jpg", img)


def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)  # find faces and eye
    coords = []
    for (x, y, w, h) in feature:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        coords = [x, y, w, h]
    return coords


def detect(img, faceCascade, img_id):
    coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face")
    if len(coords) == 4:
        x, y, w, h = coords[0], coords[1], coords[2], coords[3]
        roi_img = img[y:y + h, x:x + w]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)
    return img


img_id = 0
num_of_img = 200

while True:
    _, img = cap.read()
    img = detect(img, faceCascade, img_id)
    cv2.imshow("video", img)
    img_id += 1
    if (cv2.waitKey(1) & 0xff == ord('q')) or (img_id == num_of_img):
        break

cap.release()
cv2.destroyAllWindows()
