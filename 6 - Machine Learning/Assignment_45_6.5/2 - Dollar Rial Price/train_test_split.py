from sklearn.datasets import load_iris
import numpy as np


def train_test_split(*args, test_size=0.2, shuffle=True, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    n_samples = len(args[0])
    indices = np.arange(n_samples)

    if shuffle:
        np.random.shuffle(indices)

    test_size = int(n_samples * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]

    outputs = []
    for arg in args:
        train, test = arg[train_indices], arg[test_indices]
        outputs.append(train)
        outputs.append(test)

    return outputs


if __name__ == '__main__':
    df = load_iris()
    X = df.data
    Y = df.target
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=42)
    print(len(x_train), len(y_train))
    print(len(x_test), len(y_test))
