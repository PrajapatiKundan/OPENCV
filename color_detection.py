import cv2
import numpy as np

cap = cv2.VideoCapture(0)
width, height = 360, 360
cap.set(3, 360)  # width
cap.set(4, 360)  # height



def empty(a):
    pass  # do nothing


cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 640, 300)
cv2.createTrackbar('Hue min', 'HSV', 0, 179, empty)
cv2.createTrackbar('Hue max', 'HSV', 179, 179, empty)
cv2.createTrackbar('Sat min', 'HSV', 0, 255, empty)
cv2.createTrackbar('Sat max', 'HSV', 255, 255, empty)
cv2.createTrackbar('Val min', 'HSV', 0, 255, empty)
cv2.createTrackbar('Val max', 'HSV', 255, 255, empty)

while True:

    _, img = cap.read()
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #get trackbar value for threshold image
    h_min = cv2.getTrackbarPos('Hue min', 'HSV')
    h_max = cv2.getTrackbarPos('Hue max', 'HSV')
    s_min = cv2.getTrackbarPos('Sat min', 'HSV')
    s_max = cv2.getTrackbarPos('Sat max', 'HSV')
    v_min = cv2.getTrackbarPos('Val min', 'HSV')
    v_max = cv2.getTrackbarPos('Val max', 'HSV')

    #print(v_min)
    #threshold value
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    #create a mask for defining rule
    mask = cv2.inRange(hsvImg, lower, upper)

    res = cv2.bitwise_and(img, img, mask = mask)#pixel that are in both img & mask

    maskBgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #stack images horizontally
    hstack = np.hstack([img, maskBgr, res])
    # cv2.imshow('img', img)
    # cv2.imshow('mask', mask)
    # cv2.imshow('hscImg', hsvImg)
    cv2.imshow('result', hstack)
    if cv2.waitKey(1) & 0xff == ord('q'):  # ascii of enter key is 10
        break
