import numpy as np


class LLSRegression:
    def __init__(self):
        self.w = None

    def fit(self, x_train, y_train):
        self.w = np.linalg.pinv(x_train.T @ x_train) @ x_train.T @ y_train

    def predict(self, x_test):
        output = []
        for x in x_test:
            output.append(x @ self.w)
        return np.array(output)

    def score(self, x_test, y_test, metric):
        y_predict = self.predict(x_test)
        error = y_test - y_predict
        if metric == 'MAE':
            return np.sum(np.abs(error) / len(y_test))
        elif metric == 'MSE':
            return np.sum((error ** 2) / len(y_test))
        elif metric == 'RMSE':
            return np.sqrt(np.sum(error ** 2) / len(y_test))
        else:
            raise ValueError('Metric is invalid. please enter RMSE or MSE or MAE')
