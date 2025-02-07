import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import matplotlib.pyplot as plt
from config import *

df = pd.read_csv(SAVE_DATASET)

df['SX'] = df['SX'] / WINDOW_WIDTH
df['AX'] = df['AX'] / WINDOW_WIDTH
df['SY'] = df['SY'] / WINDOW_HEIGHT
df['AY'] = df['AY'] / WINDOW_HEIGHT

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=42)
x_test, x_validation, y_test, y_validation = train_test_split(x_test, y_test, test_size=.25, random_state=42)

print('=============== Data Shape ===============')
print(f'Train X:{x_train.shape}, Y:{y_train.shape}')
print(f'Validation X:{x_validation.shape}, Y:{y_validation.shape}')
print(f'Test X:{x_test.shape}, Y:{y_test.shape}')

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation=tf.keras.activations.relu),
    tf.keras.layers.Dense(64, activation=tf.keras.activations.relu),
    tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
    tf.keras.layers.Dense(4, activation=tf.keras.activations.softmax)
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=.001),
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=['accuracy']
)

train_result = model.fit(x_train, y_train, epochs=200, validation_data=(x_validation, y_validation))
test_result = model.evaluate(x_test, y_test)

plt.figure()
plt.plot(train_result.history['loss'], label='validation loss')
plt.plot(train_result.history['val_loss'], label='train loss')
plt.legend()
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.savefig("results/train_val_loss.png")

plt.figure()
plt.plot(train_result.history['accuracy'], label='validation accuracy')
plt.plot(train_result.history['val_accuracy'], label='train accuracy')
plt.legend()
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.savefig("results/train_val_accuracy.png")

print(f'Test result: {test_result}')

model.save('results/model.keras')
model.save('results/model.h5')
print('Model saved')