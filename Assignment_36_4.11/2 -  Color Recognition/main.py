import cv2 as cv


def color_recognition(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    rows, cols = image.shape[:2]
    h, s, v = cv.split(image)
    colors = {
        'red': 0, 'green': 0, 'blue': 0, 'yellow': 0,
        'pink': 0, 'white': 0, 'black': 0, 'turquoise': 0
    }
    for row in range(rows):
        for col in range(cols):
            if 0 <= s[row, col] < 100:
                colors['white'] += 1
            elif 0 <= v[row, col] < 100:
                colors['black'] += 1
            elif 0 <= h[row, col] < 30 / 2 or 330 / 2 <= h[row, col] <= 360 / 2:
                colors['red'] += 1
            elif 30 / 2 <= h[row, col] < 90 / 2:
                colors['yellow'] += 1
            elif 90 / 2 <= h[row, col] < 150 / 2:
                colors['green'] += 1
            elif 150 / 2 <= h[row, col] < 210 / 2:
                colors['turquoise'] += 1
            elif 210 / 2 <= h[row, col] < 270 / 2:
                colors['blue'] += 1
            elif 270 / 2 <= h[row, col] < 330 / 2:
                colors['pink'] += 1

    return max(colors, key=lambda k: colors[k])


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
