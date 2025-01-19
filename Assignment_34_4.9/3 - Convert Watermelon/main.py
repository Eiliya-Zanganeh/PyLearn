import cv2 as cv

image = cv.imread('inputs/img.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
r, g, b = cv.split(image)
output = cv.merge([b, r, g])
cv.imwrite('outputs/output.png', output)

