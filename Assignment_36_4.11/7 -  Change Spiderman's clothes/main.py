import cv2 as cv


image = cv.imread('inputs/img.png')
rows, cols = image.shape[:2]
image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
h, s, v = cv.split(image)
for row in range(rows):
    for col in range(cols):
        if 0 <= h[row, col] < 15 or 165 <= h[row, col] <= 180:
            h[row][col] += 30


image = cv.merge((h, s, v))
image = cv.cvtColor(image, cv.COLOR_HSV2BGR)
cv.imwrite('outputs/output.png', image)