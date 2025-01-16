import cv2 as cv
import numpy as np

from Modules.TFLiteFaceDetector import UltraLightFaceDetecion
from Modules.TFLiteFaceAlignment import CoordinateAlignmentModel


class FaceEffect:
    def __init__(self, image=None, center_lips=None, center_left_eye=None, center_right_eye=None):
        self.fd = UltraLightFaceDetecion("../Modules/weights/RFB-320.tflite", conf_threshold=0.88)
        self.fa = CoordinateAlignmentModel("../Modules/weights/coor_2d106.tflite")
        if image is not None:
            if center_lips is None or center_left_eye is None or center_right_eye is None:
                raise ValueError("Either center_lips, center_left_eye, center_right_eye")
        self.image = image
        self.center_lips = center_lips
        self.center_left_eye = center_left_eye
        self.center_right_eye = center_right_eye

    def get_lips_and_eyes(self, frame, draw_landmarks=False, draw_lips=False, draw_eyes=False):
        try:
            if self.image is not None:
                new_image = self.image.copy()
            else:
                new_image = None
            boxes, scores = self.fd.inference(frame)

            output = None
            for pred in self.fa.get_landmarks(frame, boxes):

                if draw_landmarks:
                    for idx, p in enumerate(np.round(pred).astype(np.int16)):
                        cv.circle(frame, tuple(p), 1, (0, 0, 255), 1, cv.LINE_AA)
                        cv.putText(frame, str(idx), tuple(p), cv.FONT_HERSHEY_SIMPLEX, .5, (125, 255, 125), 2)

                if draw_lips:
                    # get lips landmark
                    lips_landmarks = []
                    if self.center_lips is None:
                        self.center_lips = pred[60]

                    for i in [52, 55, 65, 64, 63, 71, 67, 68, 69, 61, 58, 59, 53, 56]:
                        lips_landmarks.append(pred[i])

                    if lips_landmarks:
                        output = self.draw(lips_landmarks, self.center_lips, frame, new_image)

                if draw_eyes:
                    # get lips landmark
                    left_eye_landmarks = []
                    right_eye_landmarks = []

                    if self.center_left_eye is None:
                        self.center_left_eye = pred[38]
                    if self.center_right_eye is None:
                        self.center_right_eye = pred[88]

                    for i in [35, 36, 33, 37, 39, 42, 40, 41]:
                        left_eye_landmarks.append(pred[i])

                    for i in [89, 90, 87, 91, 93, 96, 94, 95]:
                        right_eye_landmarks.append(pred[i])

                    if left_eye_landmarks:
                        output = self.draw(left_eye_landmarks, self.center_left_eye, frame, new_image)

                    if right_eye_landmarks:
                        output = self.draw(right_eye_landmarks, self.center_right_eye, frame, new_image)

                    if all(self.center_lips == pred[60]):
                        self.center_lips = None
                    if all(self.center_left_eye == pred[38]):
                        self.center_left_eye = None
                    if all(self.center_right_eye == pred[88]):
                        self.center_right_eye = None

                break

            if output is None:
                return frame
            else:
                return output
        except Exception as error:
            print(error)
            return frame

    def draw(self, landmarks, center_of_shape, frame, new_image):
        mask = np.zeros(frame.shape, dtype=np.uint8)
        lips_landmarks = np.array(landmarks, dtype=int)
        cv.drawContours(mask, [lips_landmarks], -1, (255, 255, 255), -1)
        x, y, w, h = cv.boundingRect(lips_landmarks)
        mask = mask / 255
        lips = mask * frame
        lips = lips[y:y + h, x:x + w]
        lips = cv.resize(lips, (0, 0), fx=2, fy=2)

        h, w, _ = lips.shape
        h, w = h // 2, w // 2
        x = int(center_of_shape[0] - w)
        y = int(center_of_shape[1] - h)
        if new_image is not None:
            image = new_image
        else:
            image = frame
        result = image[y:y + lips.shape[0], x:x + lips.shape[1]]
        for row_idx, row in enumerate(lips):
            for pixel_idx, pixel in enumerate(row):
                num_1, num_2, num_3 = pixel
                avg = (num_1 + num_2 + num_3) // 3
                if avg < 10:
                    lips[row_idx, pixel_idx] = result[row_idx, pixel_idx]

        image[y:y + lips.shape[0], x:x + lips.shape[1]] = lips
        return image


def main():
    cap = cv.VideoCapture(0)
    face_effect = FaceEffect()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = face_effect.get_lips_and_eyes(frame, draw_lips=True, draw_eyes=True)

        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    main()
