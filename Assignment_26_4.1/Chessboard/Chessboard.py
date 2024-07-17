import cv2 as cv
import numpy as np

chess = np.zeros([400, 400])

i = 0
for row in range(9):
    for col in range(9):
        if i % 2 == 0:
            chess[
            ((row - 1) * 50): row * 50,
            ((col - 1) * 50):  col * 50
            ] = 255
        i += 1
        # cv.imshow("Chessboard", chess)
        # cv.waitKey(100)

cv.imwrite("Chessboard.png", chess)