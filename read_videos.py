import cv2 as cv

capture = cv.VideoCapture('videos/typing.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Web Cam', frame)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
