import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
wf = img[100:300 , 130:400]
img[0:200, 0:270] = wf
cv2.imshow('Watch',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
