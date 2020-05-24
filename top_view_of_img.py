import cv2
import numpy as np

img = cv2.imread('resources/iphone.jpg')

circles = np.zeros((4,2),np.int)
count = 0
def mousePoints (event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global count
        circles[count] = x,y
        count = count + 1
        print(circles)

while True:
    if count == 4:
        width, height = 250,350
        inputPoint = np.float32([
            circles[0],
            circles[1],
            circles[2],
            circles[3]
        ])
        outputPoint = np.float32([
            [0, 0],
            [width, 0],
            [width, height],
            [0, height]
        ])
        mapMatrix = cv2.getPerspectiveTransform(inputPoint, outputPoint)
        birdView = cv2.warpPerspective(img, mapMatrix, (width, height))
        cv2.imshow('Bird View', birdView)

    for i in range(4):
        if (circles[i][0] != 0) and (circles[i][1] != 0):
            cv2.circle(img, (circles[i][0], circles[i][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mousePoints)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break


#cv2.waitKey(0)