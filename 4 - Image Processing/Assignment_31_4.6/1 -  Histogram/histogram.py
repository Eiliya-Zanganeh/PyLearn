import cv2 as cv
import matplotlib.pyplot as plt


def histogram(image_path):
    array = [0 for _ in range(256)]
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    rows, cols = image.shape
    for row in range(rows):
        for col in range(cols):
            array[image[row, col]] += 1
    assert (rows * cols) == sum(array)
    return array, range(len(array))


image_histogram, indices = histogram("inputs/patrick.jpeg")

# plt.plot(image_histogram)
# plt.hist(image_histogram)
# plt.bar(indices, image_histogram)

# plt.show()