from tensorflow.keras import layers, optimizers, models
import numpy as np
import tensorflow as tf
from data_parser import DataCollector
from fake_dataset_utils import ReadDataset

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
  model.add(layers.Dense(units = 1024, activation = 'relu'))
  model.add(layers.Dense(units = 512, activation = 'relu'))
  model.add(layers.Dense(units = 128, activation = 'relu'))
  model.add(layers.Dense(units = 16, activation = 'relu'))
  model.add(layers.Dropout(rate = 0.2))
  model.add(layers.Dense(1, activation = 'sigmoid'))

  model.compile(optimizer = optimizers.SGD(learning_rate = learning_rate),
                                            loss = "mean_squared_error",
                                            metrics = ['accuracy'])
  return model


# collector to parse input data
# collector = DataCollector()
# collector.ReadFile("C:/UNN/Мага/ИТОПР/Micro-Atomic/resources/proba.txt")

# read fake dataset
train_input, train_output, size, image_width, image_height = \
  ReadDataset("C:/UNN/Maga/ITOPR/Micro-Atomic/src/Neural Network/datasets/train.txt")
test_input, test_output, size, image_width, image_height = \
  ReadDataset("C:/UNN/Maga/ITOPR/Micro-Atomic/src/Neural Network/datasets/test.txt")

# normalization
for i in range(len(test_input)):
  test_input[i] /= np.max(test_input[i])
for i in range(len(train_input)):
  train_input[i] /= np.max(train_input[i])

# model args
learning_rate = 0.003
epochs = 150
batch_size = 300
validation_split = 0.2

# create model
model = CreateModel(image_height, image_width, learning_rate)

# train model
history = model.fit(x = train_input, y = train_output,
                    batch_size = batch_size,
                    epochs = epochs, shuffle = True,
                    validation_split = validation_split)

#test model
model.evaluate(x = test_input, y = test_output,
               batch_size = batch_size)

# PrintModelStructure(model)
# SaveModel(model)