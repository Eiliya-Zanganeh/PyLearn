import cv2 as cv
import numpy as np


def color_recognition(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    r, g, b = cv.split(image)
    red_avg = np.mean(r)
    green_avg = np.mean(g)
    blue_avg = np.mean(b)
    if red_avg > 180 and green_avg > 180 and blue_avg > 180:
        return "White"
    elif red_avg < 50 and green_avg < 50 and blue_avg < 50:
        return "Black"

    elif 178 > red_avg > 78 and green_avg < 50 and 178 > blue_avg > 78:
        return "Purple"

    elif red_avg > 180:
        if green_avg < 60 and blue_avg < 60:
            return "Red"
        elif green_avg > 170 and blue_avg < 50:
            return "Yellow"
        elif 215 > green_avg > 115 and blue_avg < 50:
            return "Orange"
    elif green_avg > 180:
        return "Green"
    elif blue_avg > 180:
        return "Blue"
    return None


if __name__ == "__main__":
    # image:

    # image = cv.imread("path")
    # cv.rectangle(image, (270, 190), (370, 290), (0, 0, 255), 2)
    # color = color_recognition(image[190: 290, 270:370])
    # if color:
    #     cv.putText(image, color, (380, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    # cv.imshow("Color Recognition", image)
    # cv.waitKey(0)

    # Webcam:

    webcam = cv.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        if ret:
            cv.rectangle(frame, (270, 190), (370, 290), (0, 0, 255), 2)
            color = color_recognition(frame[190: 290, 270:370])
            if color:
                cv.putText(frame, color, (380, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv.imshow("Color Recognition", frame)
            print(color)
            if cv.waitKey(1) & 0xFF == 27:
                break
