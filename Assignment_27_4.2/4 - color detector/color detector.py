import cv2 as cv
import numpy as np

window_size = 50


def main():
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame from video capture...")
            cv.destroyAllWindows()
            continue
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        row, col = gray.shape
        # print(f"col: {col}, row: {row}")

        Y = row // 2
        X = col // 2

        # cv.circle(gray, (X, Y), window_size, (255, 255, 255), -1)
        img = gray[Y - window_size: Y + window_size, X - window_size:X + window_size]
        cv.rectangle(gray, (X - window_size, Y - window_size), (X + window_size, Y + window_size), (0,), 5)

        avg = np.average(img)
        if 0 < avg <= 85:
            color = "Black..."
        elif 85 < avg <= 150:
            color = "Gray..."
        elif 150 < avg <= 255:
            color = "White..."
        else:
            color = None
        cv.putText(gray, color, (20, 40), cv.FONT_HERSHEY_TRIPLEX, 1, (0,), 2)
        cv.imshow('gray', gray)
        if cv.waitKey(1) & 0xFF == 27:
            break


if __name__ == '__main__':
    main()
