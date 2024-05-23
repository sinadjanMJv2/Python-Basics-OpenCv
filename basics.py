import cv2 as cv

img = cv.imread('photos/inday.jpg')
cv.imshow('Inday', img)

# converting image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# converting image to blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# converting image edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# converting image to dilating
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilate)

# converting image to eroding
erode = cv.erode(dilate, (7,7), iterations=3)
cv.imshow('Eroded', erode)

# resize image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resize) # area effect in resizing the image then if you inlarge the image use cubic or linear but suggested is cubic

# crop  image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped) 

cv.waitKey(0)