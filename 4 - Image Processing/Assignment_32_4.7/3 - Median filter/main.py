import numpy as np
import cv2 as cv


def median_filter(image):
    output = image.copy()

    rows, cols, channels = image.shape
    for channel in range(channels):
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                small = image[row - 1: row + 2, col - 1: col + 2, channel]
                sorted_values = np.sort(small, axis=None)
                mean = sorted_values[4]
                output[row, col, channel] = mean

    # output = cv.medianBlur(image, 3)
    return output


image = cv.imread('inputs/img_6.png')
output = np.hstack((
    image,
    median_filter(image)
))

cv.imwrite('outputs/output_6.jpg', output)
