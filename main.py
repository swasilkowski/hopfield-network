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

    trainFilePath = os.path.normpath(os.getcwd() + r"\data\randomtest-7x7.csv")
    #testFilePath = os.getcwd() + r"\data\small-7x7_input.csv"
    patterns = read_csv(trainFilePath)
    #testInput = read_csv(testFilePath)[0]
    testInput = patterns[6]

    dim_x = 7
    dim_y = 7

    network = HopfieldNetwork(patterns, dim_x, dim_y)
    network.Associate(testInput, True)



if(__name__ == "__main__"):
    main(sys.argv[1:])
