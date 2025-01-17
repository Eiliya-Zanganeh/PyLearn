import numpy as np
import cv2 as cv

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))


def equalize(img):
    img_1 = cv.equalizeHist(img)
    img_2 = clahe.apply(img)
    return img_1, img_2


img = cv.imread('inputs/img_3.png', cv.IMREAD_GRAYSCALE)
img_1, img_2 = equalize(img)
output = np.hstack((img, img_1, img_2))

cv.imwrite('outputs/output_3.png', output)
