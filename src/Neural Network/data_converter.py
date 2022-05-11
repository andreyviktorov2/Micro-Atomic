from math import sqrt
from PIL import Image
from data_parser import DataCollector
import numpy as np


def dispersion(data, expected_value):
    tmp_array = []
    for row in data:
        for elem in row:
            tmp_array.append((elem - expected_value)**2)
    return np.mean(tmp_array)

def save_image(data, filename, format):
    array = np.array(data, dtype=np.uint8)
    image = Image.fromarray(array)
    image.save(filename + format)


def normalize(parser):
    data = np.array(parser.matrix)
    exp_value = data.mean()
    dis = dispersion(data, exp_value)
    deviation = sqrt(dis)

    image = np.zeros(shape=(parser.ny, parser.nx))
    i = 0
    for row in data:
        j = 0
        for elem in row:
            coef = (elem - exp_value) / deviation
            pixel = (int)(128 - coef * 20)
            image[i, j] = pixel
            j += 1
        i += 1
    return image


#collector = DataCollector()
#collector.ReadFile("../../resources/NoName71.txt")
#image = normalize(collector)
#save_image(image, "output", ".png")