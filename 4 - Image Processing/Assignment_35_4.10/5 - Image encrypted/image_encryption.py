import cv2 as cv
import numpy as np


def encrypt(image_path, output_path, file_name):
    image = cv.imread(image_path)
    key = np.random.randint(0, 256, image.shape, dtype=np.uint8)

    image = cv.bitwise_xor(image, key)
    cv.imwrite(f"{output_path}/{file_name}.bmp", image)

    np.save(f"{output_path}/key.npy", key)

    print("Image Encrypted")

    return image, key


def decrypt(image_path, key_path, output_path, file_name):
    image = cv.imread(image_path)
    key = np.load(key_path)

    if key.shape != image.shape:
        raise ValueError("Shape image and key do not match")

    image = cv.bitwise_xor(image, key)
    cv.imwrite(f"{output_path}/{file_name}.png", image)
    print("Image Decrypted")

    return image
