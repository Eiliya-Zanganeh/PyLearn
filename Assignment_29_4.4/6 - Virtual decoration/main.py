import cv2 as cv

image_1 = cv.imread('image_1.png')
image_2 = cv.imread('image_2.png')
image_3 = cv.imread('image_3.png')


for row_idx, row in enumerate(image_3):
    for pixel_idx, pixel in enumerate(row):
        if all(pixel == (255, 255, 255)):
            image_1[row_idx][pixel_idx] = image_2[row_idx][pixel_idx]

cv.imwrite('output.png', image_1)

