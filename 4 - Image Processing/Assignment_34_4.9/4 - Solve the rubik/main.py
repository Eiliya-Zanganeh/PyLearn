import cv2 as cv


image = cv.imread('inputs/img.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
r, g, b = cv.split(image)

for i, row in enumerate(zip(r, g, b)):
    red_pixel, green_pixel, blue_pixel = row
    for j, pixel in enumerate(zip(red_pixel, green_pixel, blue_pixel)):
        if pixel == (0, 255, 255):
            image[i, j] = [255, 0, 0]
        if pixel == (255, 0, 255):
            image[i, j] = [0, 255, 0]
        if pixel == (0, 0, 255):
            image[i, j] = [255, 255, 0]

image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
cv.imwrite('outputs/img.png', image)

