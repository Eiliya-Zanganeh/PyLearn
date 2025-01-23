import cv2 as cv


image = cv.imread('inputs/img.png')
rows, cols = image.shape[:2]
image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
h, s, v = cv.split(image)
for row in range(rows):
    for col in range(cols):
        if 75 <= h[row][col] < 135:
            h[row][col] += 10


image = cv.merge((h, s, v))
image = cv.cvtColor(image, cv.COLOR_HSV2BGR)
cv.imwrite('outputs/output_4.png', image)