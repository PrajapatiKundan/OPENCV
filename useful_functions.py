import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('resources/lena.png')
img = cv2.resize(img, (360, 360))

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImg, (7, 7), 0)
cannyImg = cv2.Canny(blurImg, 100, 200)#for img with edges
dilationImg = cv2.dilate(cannyImg, kernel, iterations=2)
erosionImg = cv2.erode(dilationImg, kernel, iterations=2)

cv2.imshow('gray img', img)
cv2.imshow('colored img', grayImg)
cv2.imshow('blur img', blurImg)
cv2.imshow('canny img', cannyImg)
cv2.imshow('Dialtion',dilationImg)
cv2.imshow('Erosion',erosionImg)

cv2.waitKey(0)