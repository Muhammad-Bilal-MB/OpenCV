import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('buy.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('logo.png', cv2.IMREAD_COLOR)

#res = img1 + img2
#res = cv2.add(img1, img2)
#res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

imggry = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imggry, 220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
print(ret)
#cv2.imshow('Result',img1)
cv2.imshow('Mask',mask)
cv2.imshow('Mask Inv', mask_inv)
cv2.imshow('img1',img1_bg)
cv2.imshow('img2',img2_fg)
#cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()