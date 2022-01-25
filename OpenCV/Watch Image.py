import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Watch Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()