import cv2 as cv
import numpy as np


image_1 = cv.imread('image_1.png').astype(np.float16)
image_2 = cv.imread('image_2.png').astype(np.float16)

image_2 = 255 - image_2

image = image_2 + image_1
image = image.astype(np.uint8)

cv.imwrite('output.png', image)