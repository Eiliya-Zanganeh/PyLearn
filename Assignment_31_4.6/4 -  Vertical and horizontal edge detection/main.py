import cv2 as cv
import numpy as np

image = cv.imread('inputs/img.png', cv.IMREAD_GRAYSCALE)
output = image.copy()

# Horizontal kernel
kernel = np.array([[-1, -1, -1],
                   [0,  0, 0],
                   [1, 1, 1]])

# Vertical kernel
# kernel = np.array([[2, 0, -2],
#                    [2,  0, -2],
#                    [2, 0, -2]])

rows, cols = image.shape

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        small = image[row - 1: row + 2,col - 1: col + 2]
        output[row, col] = np.abs(np.sum(small * kernel))

cv.imwrite('output.png', output)