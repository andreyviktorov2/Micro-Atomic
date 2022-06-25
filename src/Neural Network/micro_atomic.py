from tensorflow.keras.models import load_model
import numpy as np
import sys
import os

from data_parser import DataCollector

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

# read input_data
if ".png" in input_file or ".jpeg" in input_file:
  collector.ReadImage(input_file)
else:
  collector.ReadFile(input_file)

# reshape input matrix
input = np.empty(shape=(1, collector.ny, collector.nx))
input[0] = collector.matrix / np.max(collector.matrix)

prediction = model.predict(input)[0][0] * 100.0

if "-f" in sys.argv:
  file_index = 1
  while os.path.exists(os.path.join(                       
      os.path.dirname(sys.argv[0]), "output" +            
      (str(file_index) if file_index > 1 else "") + ".txt")):
    file_index += 1
  file_name = os.path.join(os.path.dirname(sys.argv[0]),\
      "output" + (str(file_index) if file_index > 1 else "") + ".txt")

  with open(file_name, 'w') as file:
    file.write(input_file + "\n")
    if(prediction >= 50):
      file.write("Defect (probability " + "{:.2f}".format(prediction) + "%)")
    else:
      file.write("No defect (probability " + "{:.2f}".format(100 - prediction) + "%)")
  print("Result was stored in " + file_name)
else:
  if(prediction >= 50):
    print("Defect (probability " + "{:.2f}".format(prediction) + "%)")
  else:
    print("No defect (probability " + "{:.2f}".format(100 - prediction) + "%)")
