import numpy as np


class LLSRegression:
    def __init__(self):
        self.w = None

    def fit(self, x_train, y_train):
        self.w = np.matmul(x_train.T, x_train)
        self.w = np.linalg.inv(self.w)
        self.w = np.matmul(self.w, x_train.T)
        self.w = np.matmul(self.w, y_train)

    def predict(self, x_test):
        output = []
        for x in x_test:
            output.append(np.matmul(self.w, x))
        return np.array(output)

    def score(self, x_test, y_test, metric):
        y_predict = self.predict(x_test)
        if metric == 'RMSE':
            return np.sqrt(np.mean((y_test - y_predict) ** 2))
        elif metric == 'MSE':
            return np.mean((y_test - y_predict) ** 2)
        elif metric == 'MAE':
            return np.mean(np.abs(y_test - y_predict))
        else:
            raise ValueError('Metric is invalid. please enter RMSE or MSE or MAE')
