import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bg = np.zeros((1,65), np.float64)
fg = np.zeros((1,65), np.float64)

rect = (10,10,200,300)

cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()