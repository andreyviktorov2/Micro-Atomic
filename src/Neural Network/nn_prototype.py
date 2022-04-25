from tensorflow.keras.models import load_model
from tensorflow.keras import layers, optimizers, models
import numpy as np
import tensorflow as tf
from data_parser import DataCollector

import os
import sys


def SaveModel(model,
    path = os.path.join(os.path.dirname(sys.argv[0]), "model.h5")):
  model.save(path)

def PrintModelStructure(model,
    path = os.path.join(os.path.dirname(sys.argv[0]), "model.png")):
  print(model.summary())
  tf.keras.utils.plot_model(model, to_file = path, show_shapes = True)

def CreateModel(image_x, image_y, learning_rate):
  model = models.Sequential()

  model.add(layers.Flatten(input_shape = (image_x, image_y)))
  model.add(layers.Dense(units = 128, activation = 'relu'))
  model.add(layers.Dense(units = 32, activation = 'relu'))
  model.add(layers.Dense(units = 8, activation = 'relu'))
  model.add(layers.Dropout(rate = 0.2))
  model.add(layers.Dense(1, activation = 'sigmoid'))

  model.compile(optimizer = optimizers.Adam(learning_rate = learning_rate),
                                            loss = "sparse_categorical_crossentropy",
                                            metrics = ['accuracy'])
  return model


# collector to parse input data
collector = DataCollector()

# input parsed images - list of matrix (matrix = image)
input_data = [[[ ]]]
input_test_data = [[[ ]]]

# 1 - defect; 0 - no defect
target_data = 0
target_test_data = 0

image_x = 256
image_y = 20

# model args
learning_rate = 0.003
epochs = 50
batch_size = 4000
validation_split = 0.2


# create model
model = CreateModel(image_x, image_y, learning_rate)

PrintModelStructure(model)
SaveModel(model)

# train model
history = model.fit(x = input_data, y = target_data,
                    batch_size = batch_size,
                    epochs = epochs, shuffle = True,
                    validation_split = validation_split)

#test model
model.evaluate(x = input_test_data, y = target_test_data,
               batch_size = batch_size)