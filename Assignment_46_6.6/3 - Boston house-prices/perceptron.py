import numpy as np


class Perceptron:
    def __init__(self, weight_learning_rate: float, bias_learning_rate: float, epochs: int, num_features: int = 1) -> None:
        self.weight_learning_rate = weight_learning_rate
        self.bias_learning_rate = bias_learning_rate
        self.epochs = epochs
        self.bias = np.random.rand(1, 1)
        self.weight = np.random.rand(num_features, 1)

    def train(self, X_train: np.ndarray, Y_train: np.ndarray) -> None:
        self.losses = []
        for epoch in range(self.epochs):
            epoch_losses = []
            for x, y in zip(X_train, Y_train):
                y_pred = np.dot(x, self.weight) + self.bias
                error = y - y_pred
                loss = self.MAE_loss_function(error)
                self.SGD_optimizer(x, error)
                epoch_losses.append(loss)
            print(f'Epoch: {epoch + 1}, Loss: {np.mean(epoch_losses)}')
            self.losses.append(np.mean(epoch_losses))

    def SGD_optimizer(self, x: np.ndarray, error: np.ndarray) -> None:
        self.weight += self.weight_learning_rate * error * x.reshape(-1, 1)
        self.bias += self.bias_learning_rate * error

    def MAE_loss_function(self, error: np.ndarray) -> float:
        return np.mean(np.abs(error))

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        return np.dot(x_test, self.weight) + self.bias

    def evaluate(self, x_test: np.ndarray, y_test: np.ndarray) -> float:
        y_pred = self.predict(x_test)
        error = y_test - y_pred
        return self.MAE_loss_function(error)