import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    lower_blue = np.array([0,0,150])
    upper_blue = np.array([50,255,255])

    mask = cv2.inRange(frame ,lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kr = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kr, iterations=1)
    dilation = cv2.dilate(mask, kr, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kr)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kr)

    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Res',res)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows()
cap.release()