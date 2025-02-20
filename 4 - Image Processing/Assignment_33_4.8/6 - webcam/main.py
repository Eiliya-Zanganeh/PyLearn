import cv2 as cv


def apply_mask(image_path, image_x, image_y, w, h):
    image_original = cv.imread(image_path)
    webcam = cv.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        image = image_original.copy()
        if ret:
            center_y, center_x = frame.shape[:2]
            center_x = (center_x - w) // 2
            center_y = (center_y - h) // 2
            image[image_y:image_y + h, image_x:image_x + w] = frame[center_y:center_y + h, center_x:center_x + w]
            cv.imshow('webcam', image)
            if cv.waitKey(1) & 0xFF == 27:
                break


if __name__ == '__main__':
    apply_mask('inputs/img.png', 550, 330, 120, 70)
