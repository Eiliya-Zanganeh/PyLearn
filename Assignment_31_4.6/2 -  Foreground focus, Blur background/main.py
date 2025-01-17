import cv2 as cv
import numpy as np

image = cv.imread('inputs/img.png', cv.IMREAD_GRAYSCALE)
output = image.copy()

kernel_size = 5

padding = (kernel_size - 1) // 2

kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8) / kernel_size ** 2

rows, cols = image.shape

for row in range(padding, rows - padding):
    for col in range(padding, cols - padding):
        if image[row, col] < 200:
            small = image[
                    row - padding: row + padding + 1,
                    col - padding: col + padding + 1
                    ]
            result = np.abs(np.sum(small * kernel))
            output[row, col] = result


cv.imwrite('output_1.png', output)
