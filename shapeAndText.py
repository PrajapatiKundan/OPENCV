import cv2
import numpy as np

img = np.zeros((500, 500, 3), np.uint8)
img[:] = 0, 255, 255 #B, G, R

#vertical line
cv2.line(img, (250, 0), (250, 250), (0, 0, 255), 2)

#horizontal line
cv2.line(img, (0, 250), (500, 250), (0, 0, 255), 2)

#rectagle
width = 150
height = 150

cv2.rectangle(img, (20, 20), (20+width, 20+height), (255, 0, 255), 2)

#circle
redius = 50
cv2.circle(img, (375, 125), redius, (100, 0, 0), cv2.FILLED)

#text
cv2.putText(img, "Shapes Tutorial", (100,350), cv2.FONT_ITALIC, 1, (0, 255, 0), 3)

cv2.imshow("image", img)

cv2.waitKey(0)