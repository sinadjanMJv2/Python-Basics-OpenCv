import cv2 as cv

# img = cv.imread('photos/inday.jpg')

# cv.imshow('Inday', img)

capture = cv.VideoCapture('videos/mitsuha.mp4')

while True:

    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)