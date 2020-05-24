import cv2
import numpy as np

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerMOSSE_create()
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
# tracker = cv2.TrackerCSRT_create()

ret, img = cap.read()
box = cv2.selectROI('Image', img, False)
tracker.init(img, box)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 3, 1)
    cv2.putText(img, 'Tracking', (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    ret, img = cap.read()


    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, 'LOST', (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, 'FPS:'+str(int(fps)), (75, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()