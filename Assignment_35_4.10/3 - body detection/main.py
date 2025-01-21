import math

import cv2 as cv
import mediapipe as mp


class PoseDetector:
    def __init__(self):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpPose.Pose()

    def find_pose(self, img, draw=True):
        img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(img_RGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def get_position(self, img, draw=True):
        self.lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 3, (0, 0, 255), cv.FILLED)
        return self.lm_list

    def findAngle(self, img, p1, p2, p3, draw=True):
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        x3, y3 = self.lm_list[p3][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        # print(angle)

        if draw:
            cv.circle(img, (x1, y1), 10, (255, 0, 0), cv.FILLED)
            cv.circle(img, (x2, y2), 10, (255, 0, 0), cv.FILLED)
            cv.circle(img, (x3, y3), 10, (255, 0, 0), cv.FILLED)

            cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv.line(img, (x2, y2), (x3, y3), (255, 0, 0), 3)

        return angle


def main():
    cap = cv.VideoCapture(1)
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        detector.find_pose(img)

        cv.imshow('img', img)
        cv.waitKey(1)


if __name__ == '__main__':
    main()
