import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    lp = cv2.Laplacian(frame,cv2.CV_64F)
    sbx = cv2.Sobel(frame, cv2.CV_64F, 1,0,ksize=5)
    sby = cv2.Sobel(frame, cv2.CV_64F, 0,1,ksize=5)
    edge = cv2.Canny(frame, 100, 100)


    cv2.imshow('frame',frame)
    cv2.imshow('lap',lp)
    cv2.imshow('sbx',sbx)
    cv2.imshow('sby',sby)
    cv2.imshow('edge',edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
