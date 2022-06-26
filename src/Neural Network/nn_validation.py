from tensorflow.keras.models import load_model
import os
from fake_dataset_utils import ReadDataset

model = load_model(os.path.join("src", "Neural Network", "model.h5"))

test_input, test_output, size, image_width, image_height = \
  ReadDataset(os.path.join("resources", "validation.txt"))

model.evaluate(x = test_input, y = test_output, batch_size = 1)