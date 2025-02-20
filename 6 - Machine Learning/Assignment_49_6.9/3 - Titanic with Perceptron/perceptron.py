import numpy as np


class Perceptron:
    def __init__(self, learning_rate: float, epochs: int, num_features: int = 1, activation: str | None = None) -> None:
        self.learning_rate = learning_rate
        self.num_features = num_features
        self.epochs = epochs
        self.bias = np.random.rand(1)
        self.weight = np.random.rand(num_features)
        self.activation = activation

        self.train_losses = []
        self.train_accuracies = []
        self.validation_losses = []
        self.validation_accuracies = []

    def train(self,
              X_train: np.ndarray,
              Y_train: np.ndarray,
              X_validation: np.ndarray,
              Y_validation: np.ndarray
              ) -> None:
        for epoch in range(self.epochs):
            train_loss = []
            train_accuracy = []

            # Train model
            for x, y in zip(X_train, Y_train):
                # forward
                y_pred = x @ self.weight + self.bias
                if self.activation:
                    y_pred = self.activation_function(y_pred, self.activation)

                # backward
                error = y - y_pred
                self.SGD_optimizer(x, error)

                # save results:
                loss = self.MAE_loss_function(error)
                accuracy = self.accuracy(y, y_pred)
                train_loss.append(loss)
                train_accuracy.append(accuracy)

            # Validation model
            loss, accuracy = self.evaluate(X_validation, Y_validation)

            # save result

            self.train_losses.append(np.mean(train_loss))
            self.train_accuracies.append(np.mean(train_accuracy))
            self.validation_losses.append(loss)
            self.validation_accuracies.append(accuracy)

            print(f'Epoch: {epoch + 1}')
            print(f'Train Loss: {np.mean(train_loss)}, Train Accuracy: {np.mean(train_accuracy)}')
            print(f'Validation Loss: {loss}, Validation Accuracy: {accuracy}')

        self.train_losses = np.array(self.train_losses)
        self.train_accuracies = np.array(self.train_accuracies)
        self.validation_losses = np.array(self.validation_losses)
        self.validation_accuracies = np.array(self.validation_accuracies)
        print('Final Result:')
        print(f'Train Loss: {np.mean(self.train_losses)}, Train Accuracy: {np.mean(self.train_accuracies)}')
        print(
            f'Validation Loss: {np.mean(self.validation_losses)}, Validation Accuracy: {np.mean(self.validation_accuracies)}')

    def activation_function(self, x, func, alpha=0.01) -> np.ndarray | None:
        if func == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        elif func == 'tanh':
            return np.tanh(x)
        elif func == 'relu':
            return np.maximum(0, x)
        elif func == 'leaky_relu':
            return np.where(x > 0, x, alpha * x)
        elif func == 'elu':
            return np.where(x > 0, x, alpha * (np.exp(x) - 1))
        elif func == 'softmax':
            exp_x = np.exp(x - np.max(x))
            return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
        elif func == 'linear':
            return x
        else:
            raise ValueError(f'Unknown activation function: {func}')

    def SGD_optimizer(self, x: np.ndarray, error: np.ndarray) -> None:
        self.weight += self.learning_rate * error * x
        self.bias += self.learning_rate * error

    def MAE_loss_function(self, error: np.ndarray) -> float:
        return np.mean(np.abs(error))

    def predict(self, x_test: np.ndarray) -> np.ndarray:
        Y_pred = []
        for x in x_test:
            y_pred = x @ self.weight + self.bias
            if self.activation:
                y_pred = self.activation_function(y_pred, self.activation)
            Y_pred.append(y_pred)
        return np.array(Y_pred)

    def accuracy(self, y_test: np.ndarray, y_pred: np):
        y_pred = np.where(y_pred > .5, 1, 0)
        return np.mean(y_pred == y_test)

    def evaluate(self, x_test: np.ndarray, y_test: np.ndarray) -> float:
        y_pred = self.predict(x_test)
        error = y_test - y_pred
        loss = self.MAE_loss_function(error)
        accuracy = 0
        if self.num_features > 1:
            accuracy = self.accuracy(y_test, y_pred)
        return loss, accuracy

    def save(self, directory: str = './') -> None:
        np.save(f"{directory}/weights.npy", self.weight)
        np.save(f"{directory}/bias.npy", self.bias)

    def load_state_dict(self, model_directory: str) -> None:
        self.weight = np.load(f"{model_directory}/weights.npy").reshape(-1, 1)
        self.bias = np.load(f"{model_directory}/bias.npy")
