import cv2 as cv
import numpy as np

image = np.zeros((500, 805, 3), np.uint8)
rows, cols, channels = image.shape

section_size = cols // 7

for num in range(7):
    if num % 2 == 0:
        image[:, section_size * num:section_size * (num + 1)] = (0, 120, 0)
    else:
        image[:, section_size * num:section_size * (num + 1)] = (0, 80, 0)

distance_lines = section_size // 5

# lines
cv.rectangle(image, (distance_lines, distance_lines), (cols - distance_lines, rows - distance_lines), (255, 255, 255), 3)
cv.line(image, (cols // 2, distance_lines), (cols // 2, rows - distance_lines), (255, 255, 255), 3)

circle_radius = rows // 6

# center
cv.circle(image, (cols // 2, rows // 2), circle_radius, (255, 255, 255), 3)
cv.circle(image, (cols // 2, rows // 2), 8, (255, 255, 255), -1)

distance_gate = rows // 8

# gate left
cv.rectangle(image, (distance_lines, distance_gate * 2), (section_size + section_size // 2, distance_gate * 6), (255, 255, 255), 3)
cv.rectangle(image, (distance_lines, distance_gate * 3), (75 * section_size // 100, distance_gate * 5), (255, 255, 255), 3)
cv.circle(image, (section_size, rows // 2), 5, (255, 255, 255), -1)

# gate right
cv.rectangle(image, (section_size * 5 + section_size // 2, distance_gate * 2), (section_size * 7 - distance_lines, distance_gate * 6), (255, 255, 255), 3)
cv.rectangle(image, ((section_size * 6) + (25 * section_size // 100), distance_gate * 3), (section_size * 7 - distance_lines, distance_gate * 5), (255, 255, 255), 3)
cv.circle(image, (section_size * 6, rows // 2), 5, (255, 255, 255), -1)

cv.imshow("football", image)
cv.waitKey(0)
cv.imwrite('football.png', image)
