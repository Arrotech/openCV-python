import cv2 as cv

capture = cv.VideoCapture('videos/face_detector.mp4')

face_cascade = cv.CascadeClassifier('face_detector.xml')

while True:
    isTrue, img = capture.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.imshow("Face Detection", img)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()