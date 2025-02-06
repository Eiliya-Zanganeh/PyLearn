## MLP from scratch

- Train Number dataset with MLP

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
| Train      | 0.018512359924293304 | 0.9937369519832986 |
| Validation | 0.054891104600375176  | 0.9333333333333333 |
| Test       | 0.06994357166926642 | 0.8666666666666667 |

![image](2%20-%20MLP%20from%20scratch/outputs/img.png)