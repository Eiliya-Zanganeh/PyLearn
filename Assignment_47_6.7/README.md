## Perceptron (Perception Neuron)

- Train Perceptron in classification and regression project with activation functions

---

## 1 - Surgical

### model parameter:

| learning_rate | num features | Epochs |
|---------------|--------------|--------|
| 0.0001        | 24           | 50     |

### result:

| Activation function | Train Loss         | Train Accuracy     | Validation Loss  | Validation Accuracy |
|---------------------|--------------------|--------------------|------------------|---------------------|
| sigmoid             | 0.3050110287661392 | 0.7793901605739664 | 0.38129502377059 | 0.6764552539639882  |

![image](1%20-%20Surgical/outputs/sigmoid.png)

---

| Activation function | Train Loss         | Train Accuracy     | Validation Loss     | Validation Accuracy |
|---------------------|--------------------|--------------------|---------------------|---------------------|
| tanh                | 0.3155757428626995 | 0.7830799453365219 | 0.39028451251664364 | 0.6744154797097553  |

![image](1%20-%20Surgical/outputs/tanh.png)

---

| Activation function | Train Loss          | Train Accuracy     | Validation Loss    | Validation Accuracy |
|---------------------|---------------------|--------------------|--------------------|---------------------|
| relu                | 0.30341974486092466 | 0.7844431158182439 | 0.3671915251430592 | 0.6918126847621607  |

![image](1%20-%20Surgical/outputs/relu.png)

---

| Activation function | Train Loss         | Train Accuracy     | Validation Loss    | Validation Accuracy |
|---------------------|--------------------|--------------------|--------------------|---------------------|
| leaky_relu          | 0.2973522569613979 | 0.7839118551417833 | 0.3656087390325096 | 0.6906154259607633  |

![image](1%20-%20Surgical/outputs/leaky_relu.png)

---

| Activation function | Train Loss         | Train Accuracy     | Validation Loss     | Validation Accuracy |
|---------------------|--------------------|--------------------|---------------------|---------------------|
| elu                 | 0.2979022810307545 | 0.7862760505637172 | 0.36247913985304087 | 0.6936011824778285  |

![image](1%20-%20Surgical/outputs/elu.png)

---

| Activation function | Train Loss         | Train Accuracy     | Validation Loss    | Validation Accuracy |
|---------------------|--------------------|--------------------|--------------------|---------------------|
| softmax             | 0.7437649470447556 | 0.2562350529552443 | 0.7704918032786885 | 0.2295081967213115  |

![image](1%20-%20Surgical/outputs/softmax.png)

---

| Activation function | Train Loss          | Train Accuracy     | Validation Loss    | Validation Accuracy |
|---------------------|---------------------|--------------------|--------------------|---------------------|
| linear              | 0.32003919840010014 | 0.7837905705500511 | 0.3830413073715605 | 0.6899650631550658  |

![image](1%20-%20Surgical/outputs/linear.png)

---

## 2 - Weather forecast

### model parameter:

| learning_rate | num features | Epochs |
|---------------|--------------|--------|
| 0.0001        | 1            | 50     |

### result:

| Train Loss        | Validation Loss   | Test Loss         |
|-------------------|-------------------|-------------------|
| 8.171899237675593 | 8.314425745616843 | 7.156560791396904 |


#### Train and Validation loss

![image](2%20-%20Weather%20forecast/outputs/img.png)