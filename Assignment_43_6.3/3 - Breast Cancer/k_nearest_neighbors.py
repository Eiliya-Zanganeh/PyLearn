import numpy as np
from tqdm import tqdm


class KNearestNeighbors:
    def __init__(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, new_data, k=5):
        outputs = []
        for data in tqdm(new_data):
            distance = self.euclidean_distance(data, self.x_train)
            k_indices = np.argsort(distance)[:k]
            k_labels = self.y_train[k_indices].flatten()
            outputs.append(np.bincount(k_labels).argmax())
        return np.array(outputs)

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2, axis=1))

    def score(self, x_test, y_test, k=5):
        outputs = self.predict(x_test, k)
        accuracy = np.sum(outputs == y_test)
        return accuracy
