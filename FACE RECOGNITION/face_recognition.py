import cv2
import numpy as np

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_eye.xml")
mouthCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_smile.xml")
noseCascade = cv2.CascadeClassifier("./haarfiles/haarcascade_nose.xml")
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")


def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user." + str(id) + "." + str(img_id) + ".jpg", img)


# scalefactor is 1.03 means reduce size by 3%
# neighbour near rectangle high value ->high quality but less detection
def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbour)  # find faces and eye
    coords = []
    for (x, y, w, h) in feature:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        user_id, _ = clf.predict(gray_img[y:y + h, x:x + w])
        if user_id == 1:
            cv2.putText(img, "kundan", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords


def recognize(img, clf, faceCascade):
    color = {
        "blue": (255, 0, 0),
        "red": (0, 0, 255),
        "green": (0, 255, 0),
        "pink": (255, 0, 255)
    }
    coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "face", clf)
    return img


def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade, img_id):
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
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)
    return img


img_id = 0
while True:
    ret, img = cap.read()
    img = recognize(img, clf, faceCascade)
    cv2.imshow("img ", img)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
