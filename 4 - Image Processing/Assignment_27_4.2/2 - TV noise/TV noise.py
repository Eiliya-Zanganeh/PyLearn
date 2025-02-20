import cv2 as cv
import numpy as np
import imageio

frames = []
while True:
    array = np.random.randint(255, size=(480, 640), dtype=np.uint8)
    cv.imshow('noise', array)
    frames.append(array)
    if cv.waitKey(100) & 0xFF == 27:
        break

with imageio.get_writer("noise.gif", mode="I") as writer:
    for frame in frames:
        writer.append_data(frame)
