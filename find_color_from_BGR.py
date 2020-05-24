import numpy as np
import cv2

img = np.zeros((360, 360, 3), np.uint8)

def empty(a):
    pass

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar', 300, 150)
cv2.createTrackbar('B', 'trackbar', 0, 255, empty)
cv2.createTrackbar('G', 'trackbar', 0, 255, empty)
cv2.createTrackbar('R', 'trackbar', 0, 255, empty)

while True:
    Bval = cv2.getTrackbarPos('B', 'trackbar')
    Gval = cv2.getTrackbarPos('G', 'trackbar')
    Rval = cv2.getTrackbarPos('R', 'trackbar')
    img[:] = Bval, Gval, Rval


    cv2.imshow('BGR', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

