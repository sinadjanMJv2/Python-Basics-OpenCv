import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')

# Display the first image
cv.imshow('Window 1', blank)

# Display blank image
#blank[:] = 0, 255, 0
# Display the modified image in a different window
#cv.imshow('Window 2', blank)

# rectangle
# 1. comment the line 11 to 14 if you want to display rectangle inside the black area
#cv.rectangle(blank, (0,0) , (250,500), (0,255,0), thickness=5) 

# 2. filled all the square same result as -1
#cv.rectangle(blank, (0,0) , (250,500), (0,255,0), thickness=cv.FILLED)
 
cv.rectangle(blank, (0,0) , (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) #it specify rigth square and filled area
cv.imshow('Window 3', blank)

# 3. circle in blank 
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=cv.FILLED)
cv.imshow('Window 3', blank)

# 4. Draw a line  
cv.line(blank, (0,0) , (blank.shape[1]//2, blank.shape[0]//2), (225,255,255), thickness=3)
cv.imshow('Window 3', blank)

# 4. Write Text  
cv.putText(blank, 'HELLO', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #font ,fontsize, color,thickness (255,255) margin of this text-
cv.imshow('Text', blank)

# Wait for a key press and close all windows
cv.waitKey(0)
cv.destroyAllWindows()
