import cv2 as cv
import numpy as np

gradient = np.zeros([255, 255])

for row in range(255):
    gradient[row, :] = 255 - row

cv.imwrite('Gradient.png', gradient)
# cv.imshow('Gradient', gradient)
# cv.waitKey(0)
