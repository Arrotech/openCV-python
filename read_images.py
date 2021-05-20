import cv2 as cv

img = cv.imread('images/ppic.jpg')
cv.imshow('Profile Picture', img)

cv.waitKey(0)