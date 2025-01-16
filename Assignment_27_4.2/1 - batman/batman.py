import cv2 as cv


img = cv.imread('input.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
cv.imshow('output', thresh)
cv.waitKey(0)
cv.imwrite('output.png', thresh)
