import os
import imageio
import cv2

file_list = os.listdir('images')
file_list = sorted(file_list)


images = []
for file in file_list:
    file_path = f"images/{file}"
    img = cv2.imread(file_path)
    img = cv2.resize(img, (300, 300))
    images.append(img)

imageio.mimsave('eiliya.gif', images)


