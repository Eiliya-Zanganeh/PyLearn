import numpy as np
import cv2 as cv

# 1. Edge detection filter
edge_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# 2 - Average filter. Sharpening filter
sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# 3. Emboss filter
emboss_kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

# 4. Identity filter
identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

image = cv.imread('inputs/img.png', cv.IMREAD_GRAYSCALE)

output = np.hstack((
    cv.filter2D(image, -1, edge_kernel),
    cv.filter2D(image, -1, sharpening_kernel),
    cv.filter2D(image, -1, emboss_kernel),
    cv.filter2D(image, -1, identity_kernel),
))

cv.imwrite('outputs/output.png', output)