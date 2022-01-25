import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture('video.mp4')
sv = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Haar_Detected.mp4',sv, 20.0, (640,480))


while True:
    _ , img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)
        roi = gray[y:y+h, x:x+w]
        roi_cl = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_cl,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

    out.write(img)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

        