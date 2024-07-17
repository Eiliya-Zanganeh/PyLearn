import cv2 as cv

image = cv.imread('3.jpg')
image = cv.resize(image, (600, 400))
image = cv.rotate(image, cv.ROTATE_180)
cv.imwrite('3 output.png', image)