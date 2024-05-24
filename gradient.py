import cv2 as cv
import numpy as np

img = cv.imread('photos/inday.jpg')

# cv.imshow('Inday', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1 ,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 ,1)
combine_sobel = cv.bitwise_or(sobelx,sobely)

#cv.imshow('Sobel X',sobelx)
#cv.imshow('Sobel Y',sobely)
cv.imshow('Sobel Combined',combine_sobel)

cv.waitKey(0)