import cv2 as cv
import random
import imageio

img = cv.imread('winter.webp')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

col, row = img.shape

img[:][0] = 0

snow_count = 1

snows = []

frames = []


def set_random_snow():
    snow_row = []
    for _ in range(snow_count):
        new_snow = [random.choice(range(row)), 0]
        snow_row.append(new_snow)
    snows.append(snow_row)


def main():
    i = 0
    while True:
        __img__ = img.copy()
        for row in snows:
            for snow in row:
                cv.circle(__img__, snow, 3, (255, 255, 255), -1)
        cv.imshow('taghi', __img__)
        if i % 10 == 0:
            frames.append(__img__)
        i += 1
        for row_idx, row in enumerate(snows):
            for snow_idx, snow in enumerate(row):
                snows[row_idx][snow_idx][1] += 1
        set_random_snow()
        if cv.waitKey(1) & 0xFF == 27:
            break


if __name__ == '__main__':
    set_random_snow()
    main()
    with imageio.get_writer("snow.gif", mode="I") as writer:
        for frame in frames:
            writer.append_data(frame)
