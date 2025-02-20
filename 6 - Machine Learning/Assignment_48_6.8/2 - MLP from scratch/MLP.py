import numpy as np

np.random.seed(42)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    exps = np.exp(x)
    return exps / np.sum(exps)


def RMSD(Y_pred, Y_true):
    return np.sqrt(np.mean((Y_pred - Y_true) ** 2))


def accuracy(Y_pred, Y_true):
    return np.mean(np.argmax(Y_pred) == np.argmax(Y_true))


class Perceptron:
    def __init__(self, input_size, output_size, activation_function, learning_rate):
        self.weights = np.random.randn(input_size, output_size)
        self.bias = np.random.randn(output_size)
        self.activation_function = activation_function
        self.learning_rate = learning_rate

        self.weights_gradient = None
        self.bias_gradient = None

        self.last_output = None

    def forward(self, x) -> np.ndarray:
        x = x @ self.weights + self.bias
        x = self.activation_function(x)
        self.last_output = x.copy()
        return self.last_output

    def backward(self, output_last_layer, error):
        self.weights_gradient = output_last_layer.T @ error
        self.bias_gradient = error.reshape(-1)

    def update(self):
        self.weights -= self.learning_rate * self.weights_gradient
        self.bias -= self.learning_rate * self.bias_gradient


class MultiLayerPerceptron:
    def __init__(self, input_size, output_size, learning_rate):
        self.linear_1 = Perceptron(input_size, 128, sigmoid, learning_rate)
        self.linear_2 = Perceptron(128, 128, sigmoid, learning_rate)
        self.linear_3 = Perceptron(128, output_size, softmax, learning_rate)

    def forward(self, x):
        x = self.linear_1.forward(x)
        x = self.linear_2.forward(x)
        x = self.linear_3.forward(x)
        return x

    def backward(self, x, y_true, y_pred):
        error = -2 * (y_true - y_pred)
        self.linear_3.backward(self.linear_2.last_output, error)

        error = error @ self.linear_3.weights.T * self.linear_2.last_output * (1 - self.linear_2.last_output)
        self.linear_2.backward(self.linear_1.last_output, error)

        error = error @ self.linear_2.weights.T * self.linear_1.last_output * (1 - self.linear_1.last_output)
        self.linear_1.backward(x, error)

    def update(self):
        self.linear_1.update()
        self.linear_2.update()
        self.linear_3.update()
