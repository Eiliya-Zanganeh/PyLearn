import cv2 as cv


def balloons_detection(image_path):
    img = cv.imread(image_path)
    image = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
    image = cv.threshold(image, 200, 255, cv.THRESH_BINARY)[1]
    contours, _ = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    max_area = cv.contourArea(contours[1])
    for contour in contours:
        area = cv.contourArea(contour)
        if area > max_area // 2:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

    return img


if __name__ == "__main__":
    image = balloons_detection("inputs/img.png")
    cv.imwrite("outputs/output.png", image)
