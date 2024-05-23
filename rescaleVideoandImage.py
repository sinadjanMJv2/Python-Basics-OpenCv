import cv2 as cv

img = cv.imread('photos/inday.jpg')

def rescaleframe(frame, scale= 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def Changeres(width, height):

    capture.set(3,width)
    capture.set(4,height)



# resize_image = rescaleframe(img)
# cv.imshow('Inday', img)
# cv.imshow('Inday', resize_image)

capture = cv.VideoCapture('videos/mitsuha.mp4')

while True:

    isTrue, frame = capture.read()
    
    #frame_resolution = Changeres(frame)
    frame_resized = rescaleframe(frame)
   

    cv.imshow('Video', frame)
    cv.imshow('Video Resize',frame_resized)
    # cv.imshow('Video Resize',frame_resolution)

    if cv.waitKey(20) & 0xFF==ord('d'):
        
        break

capture.release()
cv.destroyAllWindows()