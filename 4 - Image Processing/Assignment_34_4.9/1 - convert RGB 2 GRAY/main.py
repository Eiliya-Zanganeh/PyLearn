import cv2 as cv
import numpy as np


def convert_RGB2GRAY(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    rows, cols = image.shape[:2]
    r, g, b = cv.split(image)
    output = np.zeros((rows, cols), dtype=np.uint8)
    for row in range(rows):
        for col in range(cols):
            avg = int(r[row, col]) + int(g[row, col]) + int(b[row, col])
            avg /= 3
            avg = round(avg)
            output[row, col] = avg
    return output


if __name__ == '__main__':
    img = cv.imread('inputs/img.png')
    gray = convert_RGB2GRAY(img)
    cv.imwrite('outputs/gray.png', gray)
