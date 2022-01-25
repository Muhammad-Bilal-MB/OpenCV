import numpy as np
import cv2

img = cv2.imread('img1.jpg')
temp = cv2.imread('img2.jpg',0)

imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

w,h = temp.shape[::-1]

res = cv2.matchTemplate(imgg, temp, cv2.TM_CCOEFF_NORMED)
thr = 0.90
loc = np.where(res >= thr)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,255),2)

cv2.imshow('Detected', cv2.resize(img, (640,480)))
cv2.waitKey(0)
cv2.destroyAllWindows()