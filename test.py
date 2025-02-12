import keras
from keras import layers

layer = layers.Dense(32, activation='relu')
inputs = keras.random.uniform(shape=(10, 20))
outputs = layer(inputs)