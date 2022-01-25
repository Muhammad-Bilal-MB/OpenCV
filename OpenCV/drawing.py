import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (200,200), (300,300), (255,255,255), 15)
cv2.rectangle(img, (15,25),(200,150),(0,0,255) ,5)
cv2.circle(img, (100,50), 110, (255,0,0), 5)
cv2.polylines(img, [np.array([[10,5],[20,30],[70,20],[50,10]])], True, (0,255,255), 5)

font = cv2.FONT_ITALIC
cv2.putText(img, 'BILAL', (0,130), font, 5, (200,255,255), 2, cv2.LINE_AA)
cv2.imshow('Watch Drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


