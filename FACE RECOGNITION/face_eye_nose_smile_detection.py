import cv2
import numpy as np

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_eye.xml")
mouthCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_smile.xml")
noseCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_nose.xml")


def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)  # find faces and eye
    coords = []
    for (x, y, w, h) in feature:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords


def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade):
    color = {
        "blue": (255, 0, 0),
        "red": (0, 0, 255),
        "green": (0, 255, 0),
        "pink": (255, 0, 255)
    }
    coords = draw_boundary(img, faceCascade, 1.1, 10, color["blue"], "Face")

    if len(coords) == 4:
        x, y, w, h = coords[0], coords[1], coords[2], coords[3]
        roi_img = img[y:y + h, x:x + w]
        coords = draw_boundary(roi_img, eyeCascade, 1.1, 14, color["green"], "eye")
        coords = draw_boundary(roi_img, noseCascade, 1.1, 4, color["red"], "nose")
        coords = draw_boundary(roi_img, mouthCascade, 1.2, 20, color["pink"], "mouth")
    return img


while True:

    ret, img = cap.read()
    img = detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
