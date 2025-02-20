import cv2 as cv
import numpy as np

face_detector = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_detector = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smail_detector = cv.CascadeClassifier('haarcascade_smile.xml')

cap = cv.VideoCapture(0)

poker_image = cv.imread('poker.png', cv.IMREAD_UNCHANGED)
sunglasess_image = cv.imread('sunglasses.png', cv.IMREAD_UNCHANGED)
smail_image = cv.imread('smail.png', cv.IMREAD_UNCHANGED)


def add_image_mask(image, new_image):
    alpha = new_image[:, :, 3] / 255.0
    foreground = new_image[:, :, :3]

    alpha = np.expand_dims(alpha, axis=-1)
    foreground_mask = alpha
    background_mask = 1.0 - alpha

    blended_image = foreground * foreground_mask + image * background_mask

    return blended_image.astype(np.uint8)


def main():
    state = None
    while cap.isOpened():
        try:
            ret, frame = cap.read()

            frame = cv.resize(frame, (700, 330))
            image_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            if not ret:
                print('could not read frame from webcam...')
                continue

            if not state:
                faces = face_detector.detectMultiScale(image_gray)
                if len(faces) > 0:
                    x, y, w, h = faces[0]
                    cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            elif state == 1:
                faces = face_detector.detectMultiScale(image_gray)
                if len(faces) > 0:
                    x, y, w, h = faces[0]
                    poker = cv.resize(poker_image, (w, h))
                    face = frame[y:y + h, x:x + w]
                    frame[y:y + h, x:x + w] = add_image_mask(face, poker)

            elif state == 2:
                eyes = eye_detector.detectMultiScale(image_gray)
                if len(eyes) > 1:
                    x1, y1, w1, h1 = eyes[0]
                    x2, y2, w2, h2 = eyes[1]
                    eyes = frame[y1 - w1:y2 + h2 + w1, x1 - w1:x2 + w2 + w1]
                    h, w = eyes.shape[:2]
                    w = 1 if w < 1 else w
                    h = 1 if h < 1 else h
                    sunglasess = cv.resize(sunglasess_image, (w, h))
                    frame[y1 - w1:y2 + h2 + w1, x1 - w1:x2 + w2 + w1] = add_image_mask(eyes, sunglasess)

                lip = smail_detector.detectMultiScale(image_gray, )
                if len(lip) > 0:
                    x, y, w, h = lip[0]
                    num = w // 4
                    x -= num
                    w += num * 2
                    y -= num
                    h += num * 2
                    lip = frame[y:y + h, x:x + w]
                    h, w = lip.shape[:2]
                    smail = cv.resize(smail_image, (w, h))
                    frame[y:y + h, x:x + w] = add_image_mask(lip, smail)

            elif state == 3:
                faces = face_detector.detectMultiScale(image_gray)
                if len(faces) > 0:
                    x, y, w, h = faces[0]
                    face = frame[y:y + h, x:x + w]
                    face = cv.resize(face, (5, 5))
                    face = cv.resize(face, (w, h), interpolation=cv.INTER_NEAREST)
                    frame[y:y + h, x:x + w] = face

            elif state == 4:
                num = frame.shape[1] // 2
                image_half = frame[:, num:]
                image_half = image_half[:, ::-1]
                frame[:, :num] = image_half
                cv.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 0, 0), 2)

            cv.imshow('image', frame)
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                break
            elif key == 49:
                state = 1
            elif key == 50:
                state = 2
            elif key == 51:
                state = 3
            elif key == 52:
                state = 4
            elif key != 255:
                print(key)
        except:
            continue


if __name__ == '__main__':
    main()
    cap.release()
    cv.destroyAllWindows()
