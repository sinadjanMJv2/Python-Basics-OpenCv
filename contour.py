import cv2 as cv
import numpy as np

img = cv.imread('photos/inday.jpg')
# cv.imshow('Inday', img)

# converting image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros((500, 500, 3), dtype='uint8')

# converting image to blur image
#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# converting image edge cascade
#canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny', canny)

ret, thresh =  cv.threshold(gray, 125 ,255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1,(0,0,225), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)