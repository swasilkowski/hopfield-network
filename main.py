import csv
import sys
import os
import copy
import random
from hopfield_network import HopfieldNetwork

def read_csv(filePath):
    elements = []
    with open(filePath, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            elements.append([int(i) for i in row])
    return elements

def get_inputs(elements):
    inputs = []
    for row in elements:
            [inputs.append(row[:-1])]
    return inputs

def main(argv):
    random.seed()

    trainFilePath = os.path.normpath(os.getcwd() + r"\data\\large-25x25.csv")
    patterns = read_csv(trainFilePath)

    dim_x = 25
    dim_y = 25
    testInput = random_input(dim_x*dim_y)

    network = HopfieldNetwork(patterns, dim_x, dim_y)
    network.Associate(testInput, True)

def random_input(pattern_length):
    output = []
    for i in range(pattern_length):
        output.append(adjust_input_value(random.randint(0,1)))
    return output

def adjust_input_value(value):
    if value == 0:
        return -1
    else:
        return value


if(__name__ == "__main__"):
    main(sys.argv[1:])
