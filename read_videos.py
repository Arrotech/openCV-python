import cv2 as cv

capture = cv.VideoCapture('videos/typing.mp4')

def resizeframe(frame, scale=0.5):
    """Resisze the frame of the image."""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    resized_video = resizeframe(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Frame', resized_video)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
