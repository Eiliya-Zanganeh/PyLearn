import cv2 as cv

image = cv.imread('inputs/img.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2BGRA)
rows, cols, channels = image.shape
for row in range(rows):
    for col in range(cols):
        if all(image[row, col] == [83, 84, 88, 255]):
            image[row, col] = [83, 84, 88, 0]
cv.imwrite('outputs/output.png', image)