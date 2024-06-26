import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/inday.jpg')
# cv.imshow('Inday', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank ,(img.shape[1]//2, img.shape[0]//2), 100 ,255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)

# gray_hist = cv.calcHist([gray],[0], mask ,[256], [0,256])

# Color Histogram
plt.figure()
plt.title('Gray Scale Histograms')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None ,[256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0 )