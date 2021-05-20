import cv2 as cv

img = cv.imread('images/ppic.jpg')

def resizeframe(frame, scale=0.75):
    """Resisze the frame of the image."""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = resizeframe(img)

cv.imshow('Profile Picture', img)
cv.imshow('Resized Profile Picture', resized_img)


cv.waitKey(0)
