import cv2 as cv
import numpy as np

HSV_RESULT = [35, 80, 100, 255, 0, 255]

cv.namedWindow('HSV TrackBars')
cv.resizeWindow('HSV TrackBars', 640, 240)

cv.createTrackbar('Hue Min', 'HSV TrackBars', HSV_RESULT[0], 180, lambda x: None)
cv.createTrackbar('Hue Max', 'HSV TrackBars', HSV_RESULT[1], 180, lambda x: None)
cv.createTrackbar('Sat Min', 'HSV TrackBars', HSV_RESULT[2], 255, lambda x: None)
cv.createTrackbar('Sat Max', 'HSV TrackBars', HSV_RESULT[3], 255, lambda x: None)
cv.createTrackbar('Val Min', 'HSV TrackBars', HSV_RESULT[4], 255, lambda x: None)
cv.createTrackbar('Val Max', 'HSV TrackBars', HSV_RESULT[5], 255, lambda x: None)


def update_hsv_results():
    global HSV_RESULT

    hue_min = cv.getTrackbarPos('Hue Min', 'HSV TrackBars')
    hue_max = cv.getTrackbarPos('Hue Max', 'HSV TrackBars')
    sat_min = cv.getTrackbarPos('Sat Min', 'HSV TrackBars')
    sat_max = cv.getTrackbarPos('Sat Max', 'HSV TrackBars')
    val_min = cv.getTrackbarPos('Val Min', 'HSV TrackBars')
    val_max = cv.getTrackbarPos('Val Max', 'HSV TrackBars')

    HSV_RESULT = [hue_min, hue_max, sat_min, sat_max, val_min, val_max]


if __name__ == '__main__':
    image = cv.imread('inputs/img.png')
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    background_image = cv.imread('inputs/img_1.png')
    background_image = cv.resize(background_image, (image.shape[1], image.shape[0]))
    while True:
        img = hsv_image.copy()
        update_hsv_results()
        lower = np.array([HSV_RESULT[0], HSV_RESULT[2], HSV_RESULT[4]])
        upper = np.array([HSV_RESULT[1], HSV_RESULT[3], HSV_RESULT[5]])
        mask = cv.inRange(img, lower, upper)
        mask[mask == 255] = 1
        background = cv.merge((
                background_image[:, :, 0] * mask,
                background_image[:, :, 1] * mask,
                background_image[:, :, 2] * mask
        ))
        mask[mask == 0] = 255
        mask[mask == 1] = 0
        img = cv.bitwise_and(img, img, mask=mask)
        img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

        output = background + img
        cv.imshow('img', output)
        if cv.waitKey(1) & 0xFF == 27:
            break
