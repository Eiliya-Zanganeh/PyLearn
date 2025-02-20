import os
import cv2 as cv
import numpy as np


def main():
    files = os.listdir("images")
    images = []
    for image in files:
        img = cv.imread("images/" + image)
        img = cv.resize(img, (182, 227))
        images.append(convert(img))
    img_1 = np.hstack((images[0], images[1]))
    img_2 = np.hstack((images[2], images[3]))
    output = np.vstack((img_1, img_2))
    cv.imwrite("output.png", output)


def convert(image):
    inverted = 255 - image
    blurred = cv.GaussianBlur(inverted, (21, 21), 0)
    inverted_blurred = 255 - blurred

    sketch = image / inverted_blurred
    sketch *= 255
    cv.imwrite('output.png', sketch)
    return sketch


if __name__ == "__main__":
    main()
