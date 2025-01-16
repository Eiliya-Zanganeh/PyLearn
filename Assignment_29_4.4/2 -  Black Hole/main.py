import os
import cv2 as cv
import numpy as np

directories = os.listdir('./')

images = []
for directory in directories:
    if os.path.isdir(directory):
        result = None
        files = os.listdir(directory)
        for file in files:
            image = cv.imread(directory + '/' + file).astype(np.float16)
            if result is None:
                result = np.zeros(image.shape, dtype=np.float16)
            result += image
        result = np.divide(result, len(files)).astype(np.uint8)
        images.append(result)

horizontal1 = np.hstack((images[0], images[1]))
horizontal2 = np.hstack((images[2], images[3]))
horizontal3 = np.vstack((horizontal1, horizontal2))

cv.imwrite('output.png', horizontal3)

