import cv2 as cv


def invert_color(file_name):
    image = cv.imread(file_name)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    row, col = image.shape
    for i in range(row):
        for j in range(col):
            image[i, j] = 255 - image[i, j]

    cv.imwrite(f'{file_name} output.png', image)


invert_color('1.jpg')
invert_color('2.jpg')
