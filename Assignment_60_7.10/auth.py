import cv2 as cv

from face_identification import FaceIdentification, CreateFaceBank


def create_face_bank():
    face_bank_creator = CreateFaceBank('face bank/', 'buffalo_l')
    face_bank_creator('face_bank.npy')


def authenticate():
    recognizer = FaceIdentification('buffalo_l', 'face_bank.npy', 10)
    webcam = cv.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        if ret:
            cv.imshow('frame', frame)
            cv.waitKey(1)
            names = recognizer(frame)[0]
            if len(names) > 0:
                if 'eiliya' in names:
                    cv.destroyAllWindows()
                    return True


if __name__ == '__main__':
    create_face_bank()
