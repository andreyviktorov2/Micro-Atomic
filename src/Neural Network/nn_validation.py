from tensorflow.keras.models import load_model
import os
import sys
from fake_dataset_utils import ReadDataset, ResultPrinter

root = os.path.dirname(sys.argv[0])
print()
print(root)
print()
model = load_model(os.path.join(root, "model.h5"))

test_input, test_output, size, image_width, image_height = \
  ReadDataset(os.path.join(root, "..", "..", "resources", "validation.txt"))

ResultPrinter().PrintValidation(model, test_input, test_output)