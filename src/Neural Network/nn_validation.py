from tensorflow.keras.models import load_model
import os
from fake_dataset_utils import ReadDataset, ResultPrinter

model = load_model(os.path.join("src", "Neural Network", "model.h5"))

test_input, test_output, size, image_width, image_height = \
  ReadDataset(os.path.join("resources", "validation.txt"))

ResultPrinter().PrintValidation(model, test_input, test_output)