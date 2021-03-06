import os
import sys
import numpy as np

class DatasetGenerator:

  def __init__(self):
    self.current_dir = os.path.dirname(sys.argv[0])
    self.file_name_full = ""
    self.image_width = 256
    self.image_height = 20


  def __CreateFile(self, file_name):
    if not os.path.exists(os.path.join(self.current_dir, "datasets")):
      os.mkdir(os.path.join(self.current_dir, "datasets"))

    file_index = 1
    while os.path.exists(os.path.join(                       
        self.current_dir, "datasets", file_name +            
        (str(file_index) if file_index > 1 else "") + ".txt")):
      file_index += 1

    file_name = file_name + (str(file_index) if file_index > 1 else "") + ".txt"
    self.file_name_full = os.path.join(self.current_dir, "datasets", file_name)
    open(self.file_name_full, 'w')
    print("Creating: " + self.file_name_full + " ...")


  def __WriteMatrixToFile(self, file, matrix):
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0])):
        file.write(str(matrix[i][j]))
        if j != len(matrix[0]) - 1:
          file.write(" ")
      file.write("\n")


  def GenerateDataset(self, file_name = "dataset", size = 100):
    self.__CreateFile(file_name)

    with open(self.file_name_full, 'w') as file:
      file.write(str(size) + "\n")
      file.write(str(self.image_width) + "\n")
      file.write(str(self.image_height) + "\n")

      for counter in range(0,size):
        matrix = np.random.randint(50, 60, (self.image_height, self.image_width))
        matrix = matrix / 100 # normalization

        if counter >= size / 2:
          triangle_width = np.random.randint(50,70)
          triangle_height = np.random.randint(6, 8)
          triangle_x0 = np.random.randint(0, self.image_width - triangle_width)
          triangle_y0 = np.random.randint(0, self.image_height - triangle_height)
          triangle_step = triangle_width / triangle_height / 2

          step = 0.0
          for i in range(triangle_y0, triangle_y0 + triangle_height):
            for j in range(triangle_x0 + int(step), triangle_x0 + triangle_width - int(step)):
              if triangle_x0 + step <= triangle_x0 + triangle_width - step:
                matrix[i][j] = 1.0 # np.random.randint(950, 1001) / 1000
            step += triangle_step
        
        self.__WriteMatrixToFile(file, matrix)



class ResultPrinter:
  def PrintPrediction(self, prediction, data_read_time, prediction_time):
    if(prediction >= 50):
      print("Defect (probability " + "{:.2f}".format(prediction) + "%)")
    else:
      print("No defect (probability " + "{:.2f}".format(100 - prediction) + "%)")
    print("Data reading time: " + "{:.3f}".format(data_read_time) + " seconds")
    print("Prediction time: " + "{:.3f}".format(prediction_time) + " seconds")

  def PrintValidation(self, model, test_input, test_output):
    model.evaluate(x = test_input, y = test_output, batch_size = 1)



class OutputHandler:
  def PrintPrediction(self, input_file, prediction, data_read_time, prediction_time):
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
        file.write("Defect (probability " + "{:.2f}".format(prediction) + "%)\n")
      else:
        file.write("No defect (probability " + "{:.2f}".format(100 - prediction) + "%)\n")
      file.write("Data reading time: " + "{:.3f}".format(data_read_time) + " seconds\n")
      file.write("Prediction time: " + "{:.3f}".format(prediction_time) + " seconds")
    print("Result was stored in " + file_name)



def ReadDataset(path):
  if os.path.exists(path):
    with open(path, 'r') as file:
      size = int(file.readline())
      width = int(file.readline())
      height = int(file.readline())
      input = np.empty((size, height, width))
      output = np.concatenate((np.zeros(int(size / 2)),
                               np.ones(size - int(size / 2))))

      for i in range(size):
        for j in range(height):
          input[i][j] = [float(number) for number in file.readline().split()]

    print("Dataset " + path + " was successfully read")
    return input, output, size, width, height
  else:
    print("File " + path + " does not exist")
    return np.empty((1, 1, 1)), np.zeros(1), 0, 0, 0
        



# DatasetGenerator().GenerateDataset(file_name="train", size=10000)
# DatasetGenerator().GenerateDataset(file_name="test", size=2000)

# input, output, size, image_width, image_height = \
#   ReadDataset("C:/UNN/????????/??????????/Micro-Atomic/src/Neural Network/datasets/test.txt")