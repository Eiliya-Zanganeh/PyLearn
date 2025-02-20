import cv2 as cv
import numpy as np

image = cv.imread('inputs/img.png')
rows, cols = image.shape[:2]

image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
h, s, v = cv.split(image)
h = h.astype(np.float16)

for row in range(rows):
    for col in range(cols):
        if 10 <= h[row][col] <= 75:
            h[row][col] += 130
        elif 150 <= h[row][col] <= 255 or 0 <= h[row][col] <= 15:
            h[row][col] += 60
            if h[row][col] > 255:
                h[row][col] -= 180

h = h.astype(np.uint8)

image = cv.merge((h, s, v))
image = cv.cvtColor(image, cv.COLOR_HSV2BGR)
cv.imwrite('outputs/output.png', image)
