import cv2 as cv
import numpy as np

from k_nearest_neighbors import KNearestNeighbors


class FindObject:
    def __init__(self, RGB_image, image_mask):
        x_train, y_train = self.convert_image_to_dataset(RGB_image, image_mask)
        self.knn = KNearestNeighbors(x_train, y_train)

    def convert_image_to_dataset(self, RGB_image, image_mask):
        hsv_image = cv.cvtColor(RGB_image, cv.COLOR_RGB2HSV)
        pixels = hsv_image.reshape(-1, 3)
        x_train = pixels / 255
        y_train = image_mask.reshape(-1, 1)
        y_train = y_train // 255
        return x_train, y_train

    def remove_background(self, RGB_image):
        new_image_hsv = cv.cvtColor(RGB_image, cv.COLOR_RGB2HSV)
        new_data = new_image_hsv.reshape(-1, 3) / 255
        y_predict = self.knn.predict(new_data)
        y_predict = y_predict.reshape(RGB_image.shape[:2]).astype(np.uint8)
        output = cv.bitwise_and(RGB_image, RGB_image, mask=y_predict)
        return output
