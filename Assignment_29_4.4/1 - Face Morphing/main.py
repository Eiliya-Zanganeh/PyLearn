import os
import cv2 as cv
import numpy as np
import imageio

frames = []
files = os.listdir("images")
images = []
for file in files:
    image = cv.imread("images/" + file)
    image = cv.resize(image, (182, 227))
    images.append(image)


for idx, image in enumerate(images):
    current_image = image.astype(np.float16)
    try:
        next_image = images[idx + 1].astype(np.float16)
    except IndexError:
        break
    i = 100
    while i >= 0:
        result = np.add(current_image * (i / 100), next_image * ((100 - i) / 100)).astype(np.uint8)
        cv.imshow("Result", result)
        result = cv.cvtColor(result, cv.COLOR_BGR2RGB)
        frames.append(result)
        if i == 100:
            cv.waitKey(3000)
        else:
            cv.waitKey(10)
        i -= 1


with imageio.get_writer("output.gif", mode="I") as writer:
    for frame in frames:
        writer.append_data(frame)