import cv2 as cv

img = cv.imread('photos/gf5.jpg')
cv.imshow('Inday', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('xaml/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Numbers of faces found ={len(faces_rect)}')

for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h),(0,255,0), thickness=2)

    cv.imshow('Faces Deteted',img)

cv.waitKey(0)