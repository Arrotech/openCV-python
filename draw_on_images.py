import cv2 as cv
import numpy as np

# create a blank image
blank_img = np.zeros((500,500,3), dtype='uint8')

# 1. Paint the whole image
blank_img[:] = 0,0,255

# 2. Paint a portion of the image
blank_img[200:300, 300:400] = 0,0,255

# 3. Draw rectangle
cv.rectangle(blank_img, (0,0), (250,250), (0,255,0), thickness=3)

# 4. Draw rectangle and fill the rectangle with a color (use cv.FILLED or -1)
cv.rectangle(blank_img, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)

# 5. Draw square and fill the square with a color (use cv.FILLED or -1)
cv.rectangle(blank_img, (0,0), (blank_img.shape[1]//2,blank_img.shape[0]//2), (0,255,0), thickness=cv.FILLED)

# 6. Draw a circle
cv.circle(blank_img, (250,250), 40, (255,0,0), thickness=3)

# 7. Draw a circle and fill it with a color
cv.circle(blank_img, (250,250), 40, (255,0,0), thickness=-1)

# 8. Draw line
cv.line(blank_img, (0,0), (250,250), (255,255,255), thickness=3)

# 9. Display Text
cv.putText(blank_img, "Aim", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)

cv.imshow('Blank Image', blank_img)

cv.waitKey(0)