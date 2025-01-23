import cv2 as cv
import numpy as np


img = cv.imread('inputs/img.png')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array([0, 48, 80], dtype="uint8")
upper = np.array([20, 255, 255], dtype="uint8")

mask = cv.inRange(img, lower, upper)
img = cv.bitwise_and(img, img, mask=mask)
img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.imwrite('outputs/img.png', img)


