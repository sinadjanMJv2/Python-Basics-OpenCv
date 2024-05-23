import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/inday.jpg')
cv.imshow('Inday', img)

# plt.imshow(img)
# plt.show()

# converting image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)


# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# HSV to BGR 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)