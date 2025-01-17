import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('inputs/img.tif', cv.IMREAD_GRAYSCALE)


kernels = [
    np.ones((5, 5), np.uint8) * .04,
    np.ones((5, 5), np.uint8) * 1,
    np.ones((5, 5), np.uint8) * 5,
    np.ones((3, 3), np.uint8) * .04,
    np.ones((3, 3), np.uint8) * 1,
    np.ones((3, 3), np.uint8) * 5,
]

filtered_images = [cv.filter2D(image, -1, kernel) for kernel in kernels]

fig, axes = plt.subplots(1, len(filtered_images), figsize=(15, 5))

for ax, img, kernel in zip(axes, filtered_images, kernels):
    ax.imshow(img, cmap='gray')
    ax.set_title(f'Avg-kernel:\n{kernel.shape} : {kernel[0][0]}')
    ax.axis('off')

plt.tight_layout()
plt.show()
