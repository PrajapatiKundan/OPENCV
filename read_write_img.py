# reading and saving the image

import cv2
import numpy as np

grey_img = cv2.imread('resources/lena.png', 0)#pass '0' for grayscale color in img

cv2.imshow('lena', grey_img)

print(grey_img.shape)

key = cv2.waitKey(0) & 0xff

#press enter for destroy, ASCII of ENTER = 10
if key == 10:
    cv2.destroyAllWindows()

#save image
elif key == ord('s'):
    cv2.imwrite('resources/lenagreyimg.png', grey_img)
    cv2.destroyAllWindows()
