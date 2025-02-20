import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm


class KNearestNeighbors:
    def __init__(self, x_train: pd.DataFrame, y_train: pd.Series):
        self.x_train = x_train
        self.y_train = y_train
        self.x_train.columns = ['x', 'y']

    def draw_dataset(self):
        labels = self.y_train.astype('category').cat.codes
        plt.scatter(self.x_train['x'], self.x_train['y'], c=labels)
        plt.show()

    def predict(self, new_data: pd.DataFrame, k=5):
        new_data.columns = ['x', 'y']
        outputs = []
        for idx, data in tqdm(new_data.iterrows(), total=len(new_data), desc="Processing Data"):
            result = self.x_train.copy()
            result['label'] = self.y_train
            result['distance'] = result.apply(lambda row: self.euclidean_distance([row['x'], row['y']], [data['x'], data['y']]), axis=1)
            result = result.sort_values(by='distance')
            result = result[:k]
            outputs.append(result['label'].value_counts().idxmax())
        return outputs

    def euclidean_distance(self, point_1, point_2):
        point_1 = np.array(point_1)
        point_2 = np.array(point_2)
        return np.sqrt(np.sum((point_1 - point_2) ** 2))

    def score(self, x_test, y_test, k=5, confusion_matrix=False):
        y_predict = self.predict(x_test, k)
        result = np.sum(y_predict == y_test) / len(x_test)
        if confusion_matrix:
            classes = self.y_train.unique().tolist()
            matrix = np.zeros((len(classes), len(classes)))
            for y_true, y_pred in zip(y_test, y_predict):
                true_idx = classes.index(y_true)
                pred_idx = classes.index(y_pred)
                matrix[true_idx, pred_idx] += 1
            plt.imshow(matrix, interpolation='nearest', cmap='Blues')
            plt.colorbar()
            plt.title(f'Confusion Matrix: Accuracy: {round(result * 100)}%')
            plt.xlabel('Predicted Labels')
            plt.ylabel('True Labels')
            plt.show()
        return result

def generate_dataset(num):
    x_apples = np.array([
        np.random.normal(6, 1, num),
        np.random.normal(6, 1, num),
    ])

    y_apples = np.array([
        np.array(['apple'] * num)
    ])

    x_bananas = np.array([
        np.random.normal(4, 1, num),
        np.random.normal(8, 1, num),
    ])

    y_bananas = np.array([
        np.array(['banana'] * num)
    ])

    x_apples = x_apples.T
    x_bananas = x_bananas.T

    x_train = pd.DataFrame(np.concatenate([x_apples, x_bananas]))
    y_train = pd.Series(np.concatenate([y_apples.reshape(-1), y_bananas.reshape(-1)]))

    x_train.columns = ['x', 'y']

    return x_train, y_train


if __name__ == "__main__":
    x_train, y_train = generate_dataset(100)

    model = KNearestNeighbors(x_train, y_train)

    # model.draw_dataset()

    x_test, y_test = generate_dataset(20)

    # print(model.predict(x_test))

    # print(model.score(x_test, y_test, confusion_matrix=True))
