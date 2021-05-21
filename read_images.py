import cv2 as cv

img = cv.imread('images/ppic.jpg')

def resizeframe(frame, scale=0.75):
    """Resisze the frame of the image."""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_img = resizeframe(img)

# gray scale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur image - remove some of the noise i.e light
blur_img = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

# edge cascade
canny_img = cv.Canny(blur_img, 125, 175)

# dilating image edges
dilated_img = cv.dilate(canny_img, (3,3), iterations=3)

# eroding dilated images to get the original edges
eroded_img = cv.erode(dilated_img, (3,3), iterations=3)

# resizing the image
resized_img2 = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

# cropping

cropped_img = img[50:200, 200:400]

cv.imshow('Profile Picture', img)
# cv.imshow('Resized Profile Picture', resized_img)
# cv.imshow("Gray Scale Image", gray_img)
# cv.imshow("Blurred Image", blur_img)
# cv.imshow("Canny Edge Cascade Image", canny_img)
# cv.imshow("Dilated Image", dilated_img)
# cv.imshow("Eroded Image", eroded_img)
# cv.imshow("Resized Image", resized_img2)
cv.imshow("Cropped Image", cropped_img)

cv.waitKey(0)
