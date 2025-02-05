import numpy as np

from perceptron import Perceptron

model = Perceptron(learning_rate=.0001, epochs=50, num_features=1)

model.load_state_dict('model')


def predict(new_input):
    normalize_data = np.array([new_input / 366]).reshape(-1, 1)
    return model.predict(normalize_data)[0][0]


if __name__ == '__main__':
    print(predict(10))
    print(predict(100))
