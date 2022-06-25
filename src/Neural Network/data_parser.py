import numpy as np
import imageio
from PIL import Image

class DataCollector(object):
    
  def __init__(self):
    self.nx = 0
    self.ny = 0
    self.scale_x = 0.0
    self.scale_y = 0.0
    self.scale_data = 0.0
    self.bias_x = 0.0
    self.bias_y = 0.0
    self.bias_data = 0.0
    self.unit_x = ""
    self.unit_y = ""
    self.unit_data = ""
    self.data_scale_needed = False
    self.matrix = np.empty(shape=(1,1))

  def ReadFile(self, path):
    with open(path, "r") as file:
      self.data = file.readlines()
    self.__ParseData()
  
  def ReadImage(self, path):
    image = Image.open(path)
    matrix = np.array(image.getdata()).reshape((image.height, image.width))
    self.matrix = matrix
    self.ny = image.height
    self.nx = image.width
    
  
  def __ParseData(self):
    for line in self.data:
      if "NX" in line:
        self.nx = (int)(line.split()[-1])
      elif "NY" in line:
        self.ny = (int)(line.split()[-1])
      elif "Scale X" in line:
        self.scale_x = (float)(line.split()[-1].replace(',', '.'))
      elif "Scale Y" in line:
        self.scale_y = (float)(line.split()[-1].replace(',', '.'))
      elif "Scale Data" in line:
        self.scale_data = (float)(line.split()[-1].replace(',', '.'))
      elif "Bias X" in line:
        self.bias_x = (float)(line.split()[-1].replace(',', '.'))
      elif "Bias Y" in line:
        self.bias_y = (float)(line.split()[-1].replace(',', '.'))
      elif "Bias Data" in line:
        self.bias_data = (float)(line.split()[-1].replace(',', '.'))
      elif "Unit X" in line:
        self.unit_x = (str)(line.split()[-1])
      elif "Unit Y" in line:
        self.unit_y = (str)(line.split()[-1])
      elif "Unit Data" in line:
        self.unit_data = (str)(line.split()[-1])
      elif "DataScaleNeeded" in line:
        if "Yes" in line.split()[-1]:
          self.data_scale_needed = True
      elif "Start of Data" in line:
        self.matrix = np.empty(shape=(self.ny, self.nx))

        idx = self.data.index(line) + 1
        idx_matrix = 0
        assert(idx <= len(self.data) and idx >= 0)

        while idx < len(self.data):
          assert(idx_matrix < self.ny)
          self.matrix[idx_matrix] = np.array(self.data[idx].split(' ')).astype(np.float)
          idx += 1
          idx_matrix += 1