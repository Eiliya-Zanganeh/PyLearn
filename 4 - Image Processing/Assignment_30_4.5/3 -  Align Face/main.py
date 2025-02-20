import cv2
import numpy as np
from mtcnn import MTCNN

detector = MTCNN()


def align_face(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = detector.detect_faces(image_rgb)

    if results:
        result = results[0]
        keypoints = result['keypoints']

        left_eye = keypoints['left_eye']
        right_eye = keypoints['right_eye']

        dY = right_eye[1] - left_eye[1]
        dX = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(dY, dX))

        eyes_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)

        rot_mat = cv2.getRotationMatrix2D(eyes_center, angle, scale=1.0)

        aligned_image = cv2.warpAffine(image, rot_mat, (image.shape[1], image.shape[0]))

        return aligned_image

    return None


image = cv2.imread('image_1.png')

if image is None:
    print("Failed to load image!")
else:
    aligned_image = align_face(image)

    if aligned_image is not None:
        cv2.imshow("Original", image)
        cv2.imshow("Aligned", aligned_image)
        cv2.waitKey(0)
    else:
        print("No face detected!")
