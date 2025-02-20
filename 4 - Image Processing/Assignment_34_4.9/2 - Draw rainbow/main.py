import cv2 as cv
import numpy as np

r = np.zeros((300, 400), dtype=np.uint8)
g = np.zeros((300, 400), dtype=np.uint8)
b = np.zeros((300, 400), dtype=np.uint8)

# Red => (255, 0, 0)
cv.circle(r, (200, 300), 150, 255, -1)
cv.circle(g, (200, 300), 130, 0, -1)
cv.circle(b, (200, 300), 130, 0, -1)

# Orange => (255, 165, 0)
cv.circle(r, (200, 300), 130, 255, -1)
cv.circle(g, (200, 300), 130, 165, -1)
cv.circle(b, (200, 300), 130, 0, -1)

# Yellow => (255, 255, 0)
cv.circle(r, (200, 300), 110, 255, -1)
cv.circle(g, (200, 300), 110, 255, -1)
cv.circle(b, (200, 300), 110, 0, -1)

# Green => (0, 128, 0)
cv.circle(r, (200, 300), 90, 0, -1)
cv.circle(g, (200, 300), 90, 128, -1)
cv.circle(b, (200, 300), 90, 0, -1)

# Turquoise => (0, 255, 255)
cv.circle(r, (200, 300), 70, 0, -1)
cv.circle(g, (200, 300), 70, 255, -1)
cv.circle(b, (200, 300), 70, 255, -1)

# Blue => (0, 0, 255)
cv.circle(r, (200, 300), 50, 0, -1)
cv.circle(g, (200, 300), 50, 0, -1)
cv.circle(b, (200, 300), 50, 255, -1)

# Purple => (128, 0, 128)
cv.circle(r, (200, 300), 30, 128, -1)
cv.circle(g, (200, 300), 30, 0, -1)
cv.circle(b, (200, 300), 30, 128, -1)

# Black => (0, 0, 0)
cv.circle(r, (200, 300), 10, 0, -1)
cv.circle(g, (200, 300), 10, 0, -1)
cv.circle(b, (200, 300), 10, 0, -1)

image = cv.merge([b, g, r])
cv.imwrite('outputs/rainbow.jpg', image)
