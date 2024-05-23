import cv2 as cv

img = cv.imread('photos/inday.jpg')
cv.imshow('Inday', img)

# Average blur
average = cv.blur(img, (3,3))
# cv.imshow('Average', average)

# Gussian blur
gussian = cv.GaussianBlur(img, (3,3), 0)
# cv.imshow('Gussian', gussian)

# Meddian blur
meddian = cv.medianBlur(img, 3)
# cv.imshow('Meddian', meddian)

# Bilateral blur
beliteral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', beliteral)

cv.waitKey(0)

