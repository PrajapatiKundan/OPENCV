import cv2

width, height = 400, 400
img = cv2.imread('resources/road.jpeg')
resizedImg = cv2.resize(img,(width,height))
croppedImg = img[150:333, 220:280]# [height,width]
cropResizeImg = cv2.resize(croppedImg,(img.shape[1], img.shape[0]))

print(resizedImg.shape)
print('original img size ',img.shape)

cv2.imshow('resized img', resizedImg)
cv2.imshow('original img', img)
cv2.imshow('cropped img', croppedImg)
cv2.imshow('cropped resized img', cropResizeImg)

cv2.waitKey(0)