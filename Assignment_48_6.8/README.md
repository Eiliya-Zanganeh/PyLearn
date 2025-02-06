## MLP from scratch

- Train Mnist dataset with MLP

## Model:

- layer 1: 64 to 128 size.
- layer 2: 128 to 128 size.
- layer 3: 128 to 10 size.
- optimizer: SGD.
- Loss function: RMSD.
- Activation functions: Sigmoid and Softmax for layer 3.
- Epochs: 50.
- Learning rate: .001.

### results:

| Data       | Loss                | Accuracy           |
|------------|---------------------|--------------------|
| Train      | 0.01812963982030111 | 0.9951287404314544 |
| Validation | 0.0838418949472025  | 0.8111111111111111 |
| Test       | 0.07259728231787792 | 0.8666666666666667 |

![image](2%20-%20MLP%20from%20scratch/outputs/img.png)