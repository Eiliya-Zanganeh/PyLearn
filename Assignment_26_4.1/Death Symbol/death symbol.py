import cv2 as cv
import numpy as np

image = np.full([400, 400], 255)

i = 0
while i <= 150:
    image[i, 100 - i:150 - i] = 0
    i += 1
# print(f'I = {i}')
i = 100
j = 50
while j > 0:
    image[i, 0:j] = 0
    j -= 1
    i += 1

cv.imwrite('death symbol.png', image)
