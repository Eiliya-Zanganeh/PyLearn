import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))


def equalize(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    # plt.plot(hist)
    # plt.show()
    equalize_hist = cv.equalizeHist(img)
    # hist = cv.calcHist([equalize_hist], [0], None, [256], [0, 256])
    # plt.plot(hist)
    # plt.show()
    equalize_clahe = clahe.apply(img)
    # hist = cv.calcHist([equalize_clahe], [0], None, [256], [0, 256])
    # plt.plot(hist)
    # plt.show()
    cv.imwrite('outputs/equalize.png', np.hstack([equalize_hist, equalize_clahe]))


img = cv.imread('inputs/img.png', cv.IMREAD_GRAYSCALE)
equalize(img)
