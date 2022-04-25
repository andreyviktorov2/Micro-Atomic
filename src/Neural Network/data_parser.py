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
    self.matrix = []

  def ReadFile(self, path):
    with open(path, "r") as file:
      self.data = file.readlines()
    self.ParseData()
  
  def ParseData(self):
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
        idx = self.data.index(line) + 1
        assert(idx <= len(self.data) and idx >= 0)
        while idx < len(self.data):
          self.matrix.append([int(number) for number in self.data[idx].split(" ")])
          idx += 1