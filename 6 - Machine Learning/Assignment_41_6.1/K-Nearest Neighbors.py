import numpy as np
import matplotlib.pyplot as plt


class KNearestNeighbors:
    def __init__(self, data):
        self.dataset = data
        self.num_classes = len(self.dataset)

    def draw_dataset(self):
        classes = []
        for idx, data in enumerate(self.dataset):
            plt.scatter(data[:, 0], data[:, 1])
            classes.append(data[:, 2][0])
        plt.legend(classes)
        plt.show()

    def predict(self, new_x, new_y, k=5):
        result = []
        for class_name in self.dataset:
            for data in class_name:
                row = [data[0], data[1], self.euclidean_distance(data[:2], np.array([new_x, new_y])), data[2]]
                result.append(row)
        result = sorted(result, key=lambda x: x[2])
        result = result[:k]
        result = list(map(lambda x: x[3], result))
        unique, counts = np.unique(result, return_counts=True)
        result = dict(zip(unique, counts))
        return max(result)

    def euclidean_distance(self, point_1, point_2):
        return np.sqrt(np.sum((point_1 - point_2) ** 2))


if __name__ == "__main__":
    num = 100
    apples = np.array([
        np.random.normal(6, 1, num),
        np.random.normal(6, 1, num),
        np.array(['apple'] * num)
    ], dtype=object)
    bananas = np.array([
        np.random.normal(4, 1, num),
        np.random.normal(8, 1, num),
        np.array(['banana'] * num)
    ], dtype=object)
    watermelons = np.array([
        np.random.normal(15, 1, num),
        np.random.normal(20, 1, num),
        np.array(['watermelon'] * num)
    ], dtype=object)

    apples = apples.T
    bananas = bananas.T
    watermelons = watermelons.T

    dataset = np.concatenate([[apples], [bananas], [watermelons]])

    model = KNearestNeighbors(dataset)

    model.draw_dataset()

    output = model.predict(5, 5)
    print(output)

    output = model.predict(12, 18)
    print(output)

    output = model.predict(5, 9)
    print(output)
