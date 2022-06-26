from tensorflow.keras.models import load_model
import numpy as np
import sys
import os
import time

from data_parser import DataCollector
from fake_dataset_utils import ResultPrinter, OutputHandler

# argv[1] is absolut path to input file
if len(sys.argv) < 2:
  print("No input file")
  sys.exit(1)
input_file = sys.argv[1]

if not os.path.exists(input_file):
  print("Input file doesn't exist")
  sys.exit(1)

# open saved model
model = load_model(os.path.join(os.path.dirname(sys.argv[0]), "model.h5"))

# collector to parse input data
collector = DataCollector()

data_read_time = time.time()

# read input_data
if ".png" in input_file or ".jpeg" in input_file:
  collector.ReadImage(input_file)
else:
  collector.ReadFile(input_file)

data_read_time = time.time() - data_read_time

# reshape input matrix
input = np.empty(shape=(1, collector.ny, collector.nx))
input[0] = collector.matrix / np.max(collector.matrix)

prediction_time = time.time()
prediction = model.predict(input)[0][0] * 100.0
prediction_time = time.time() - prediction_time

if "-f" in sys.argv:
  OutputHandler().PrintPrediction(input_file, prediction, data_read_time, prediction_time)
else:
  ResultPrinter().PrintPrediction(prediction, data_read_time, prediction_time)