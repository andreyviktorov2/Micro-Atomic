from tensorflow.keras.models import load_model
import numpy as np
import sys
import os

from data_parser import DataCollector

# argv[1] is absolut path to input file
assert(len(sys.argv) >= 2)
input_file = sys.argv[1]

# open saved model
model = load_model(os.path.join(os.path.dirname(sys.argv[0]), "model.h5"))

# collector to parse input data
collector = DataCollector()
collector.ReadFile(input_file)

# reshape input matrix
input = np.empty(shape=(1, collector.ny, collector.nx))
input[0] = collector.matrix / np.max(collector.matrix)

prediction = model.predict(input)[0][0] * 100.0

if(prediction >= 50):
  print("Defect (probability " + "{:.2f}".format(prediction) + "%)")
else:
  print("No defect (probability " + "{:.2f}".format(100 - prediction) + "%)")
