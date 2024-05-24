import cv2 as cv

img = cv.imread('photos/inday.jpg')

cv.imshow('Inday', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Simple thresholding 
threshold, thresh =  cv.threshold(gray, 150 ,255, cv.THRESH_BINARY)
# cv.imshow('Simple Threshold',thresh)

threshold, thresh_inv =  cv.threshold(gray, 150 ,255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Threshold Inverse',thresh_inv)

# Adopted thresholding 
adoptive_thresh =  cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adopted Threshold ',adoptive_thresh)


cv.waitKey(0)