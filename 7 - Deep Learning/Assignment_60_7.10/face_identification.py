import os
from tqdm import tqdm

import numpy as np
import cv2 as cv
from insightface.app import FaceAnalysis
from onnxruntime import get_available_providers


class CreateFaceBank:
    def __init__(self, face_bank_path, model_name):
        self.face_bank_path = face_bank_path
        self.app = FaceAnalysis(name=model_name, providers=get_available_providers())
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def __call__(self, save_path):
        face_bank = list()
        for person_name in tqdm(os.listdir(self.face_bank_path)):
            dir_path = os.path.join(self.face_bank_path, person_name)
            if os.path.isdir(dir_path):
                for image_name in os.listdir(dir_path):
                    image_path = os.path.join(dir_path, image_name)
                    image = cv.imread(image_path)
                    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                    result = self.app.get(image)
                    if len(result) == 1:
                        result = result[0]['embedding']
                        new_data = {'name': person_name, 'embedding': result}
                        face_bank.append(new_data)
                    else:
                        print(f'Image: {image_path} no have face or have more than one face')
        np.save(save_path, face_bank)
        print(f'Face bank saved to {save_path}')


class FaceIdentification:
    def __init__(self, model_name, face_bank, threshold):
        self.face_bank = np.load(face_bank, allow_pickle=True)
        self.threshold = threshold
        self.app = FaceAnalysis(name=model_name, providers=get_available_providers())
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def __call__(self, image):
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = self.app.get(image)
        names = list()
        for result in results:
            x1, y1, x2, y2 = result.bbox
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
            for face in self.face_bank:
                face_bank_embedding = face['embedding']
                person_embedding = result['embedding']
                distance = np.sqrt(np.sum((face_bank_embedding - person_embedding)) ** 2)
                if distance < self.threshold:
                    cv.putText(
                        image,
                        face['name'],
                        (x1 - 50, y1 - 10),
                        cv.FONT_HERSHEY_SIMPLEX,
                        8,
                        (0, 0, 255),
                        8,
                        cv.LINE_AA
                    )
                    names.append(face['name'])
                    break
            else:
                cv.putText(
                    image,
                    'Unknown',
                    (x1 - 50, y1 - 10),
                    cv.FONT_HERSHEY_SIMPLEX,
                    8,
                    (0, 0, 255),
                    8,
                    cv.LINE_AA
                )
        return names, image