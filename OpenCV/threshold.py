import numpy as np 
import cv2

img = cv2.imread('book.jpg')
imggry = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imggry, 100, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(imggry, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('image',imggry)
cv2.imshow('threshold',thresh)
cv2.imshow('Gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()