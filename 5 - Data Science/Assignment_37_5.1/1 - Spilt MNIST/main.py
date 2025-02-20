import os
import cv2 as cv

image = cv.imread('img.png', cv.IMREAD_GRAYSCALE)
rows, cols = image.shape

if not os.path.exists('MNIST'):
    os.makedirs('MNIST')

for num, i in enumerate(range(0, rows, 40)):
    image_rows = image[i:i + 40, :]
    directory = f'MNIST/{num}'
    if not os.path.exists(directory):
        os.makedirs(directory)

    row, col = image_rows.shape
    file_name = 1
    for r in range(0, row, 8):
        for c in range(0, col, 8):
            cv.imwrite(f'{directory}/image_{file_name}.png', image_rows[r:r + 8, c: c + 8])
            file_name += 1
