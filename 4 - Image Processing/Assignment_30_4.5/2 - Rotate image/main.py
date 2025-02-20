import cv2 as cv
import numpy as np
from Modules.TFLiteFaceDetector import UltraLightFaceDetecion
from Modules.TFLiteFaceAlignment import CoordinateAlignmentModel


class FaceEffect:
    def __init__(self):
        self.fd = UltraLightFaceDetecion("../Modules/weights/RFB-320.tflite", conf_threshold=0.88)
        self.fa = CoordinateAlignmentModel("../Modules/weights/coor_2d106.tflite")

    def rotate_lips_and_eyes(self, frame):
        # Create a copy of the frame to apply the transformations
        new_image = frame.copy()

        # Detect face landmarks
        boxes, scores = self.fd.inference(frame)

        for pred in self.fa.get_landmarks(frame, boxes):
            # Rotate lips
            lips_landmarks = pred[[52, 55, 65, 64, 63, 71, 67, 68, 69, 61, 58, 59, 53, 56]]
            new_image = self.process_and_rotate(lips_landmarks, frame, new_image, scale_factor=1.2)

            # Rotate left eye
            left_eye_landmarks = pred[[35, 36, 33, 37, 39, 42, 40, 41]]
            new_image = self.process_and_rotate(left_eye_landmarks, frame, new_image, scale_factor=1.2)

            # Rotate right eye
            right_eye_landmarks = pred[[89, 90, 87, 91, 93, 96, 94, 95]]
            new_image = self.process_and_rotate(right_eye_landmarks, frame, new_image, scale_factor=1.2)

        return new_image

    def process_and_rotate(self, landmarks, frame, new_image, scale_factor=1.2):
        # Create a mask for the selected region (lips or eyes)
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        landmarks = np.array(landmarks, dtype=np.int32)

        # Fill the mask with the region of interest
        cv.fillPoly(mask, [landmarks], 255)

        # Extract the region using the mask
        extracted_region = cv.bitwise_and(frame, frame, mask=mask)

        # Get bounding box of the landmarks to crop the region
        x, y, w, h = cv.boundingRect(landmarks)
        cropped_region = extracted_region[y:y + h, x:x + w]

        # Resize (enlarge) the cropped region
        new_size = (int(w * scale_factor), int(h * scale_factor))
        enlarged_region = cv.resize(cropped_region, new_size)

        # Rotate the enlarged region 180 degrees
        rotated_region = cv.rotate(enlarged_region, cv.ROTATE_180)

        # Calculate the new position for pasting the rotated region
        new_x = x - (new_size[0] - w) // 2
        new_y = y - (new_size[1] - h) // 2

        # Ensure the new position is within image bounds
        new_x = max(new_x, 0)
        new_y = max(new_y, 0)

        # Get the size of the rotated region
        h_rotated, w_rotated = rotated_region.shape[:2]

        # Adjust the size of new_image slice to match the rotated_region size
        if new_y + h_rotated <= new_image.shape[0] and new_x + w_rotated <= new_image.shape[1]:
            # Create a mask to identify black pixels in the rotated region
            black_mask = (rotated_region[:, :, 0] == 0) & (rotated_region[:, :, 1] == 0) & (
                    rotated_region[:, :, 2] == 0)

            # Replace black pixels in rotated_region with corresponding pixels from the original frame
            for c in range(3):  # For each color channel
                rotated_region[black_mask, c] = frame[new_y:new_y + h_rotated, new_x:new_x + w_rotated][black_mask, c]

            # Directly place the rotated region in the new image
            new_image[new_y:new_y + h_rotated, new_x:new_x + w_rotated] = rotated_region

        return new_image


def main():
    # Load the input image
    image = cv.imread('./image.png')

    # Create an instance of FaceEffect
    face_effect = FaceEffect()

    # Apply the rotation effect to lips and eyes
    output_image = face_effect.rotate_lips_and_eyes(image)

    # Save and display the result
    cv.imwrite('./rotated_image.png', output_image)
    cv.imshow('Rotated Image', output_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
