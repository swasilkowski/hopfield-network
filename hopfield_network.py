import random
import copy
from visualize_gui import visualize

class HopfieldNetwork:
    def __init__(self, patterns, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        pattern_length = dim_x * dim_y
        self.weights = [[0 for i in range(pattern_length)] for i in range(pattern_length)]

        for i in range(pattern_length):
            for j in range(pattern_length):
                if (i==j):
                    continue
                x=0
                for k in patterns:
                    x+=k[i]*k[j]
                self.weights[i][j] = float(x)/pattern_length

    def Associate(self, _input, is_synchronous):
        pattern_length = _input.__len__()
        _input = visualize(_input, self.dim_x, self.dim_y, True)
        self.output = copy.deepcopy(_input)

        is_stable = False
        while(not is_stable):
            if is_synchronous:
                for i in range(pattern_length):
                    f = 0
                    for j in range(pattern_length):
                        f += self.weights[i][j] * _input[j]
                    if f > 0:
                        self.output[i] = 1
                    elif f < 0:
                        self.output[i] = -1
                    else:
                        self.output[i] = _input[i]
            else:
                for i in random.shuffle(range(pattern_length)):
                    f = 0
                    for j in range(pattern_length):
                        f += self.weights[i][j] * _input[j]
                    if f > 0:
                        self.output[i] = 1
                    elif f < 0:
                        self.output[i] = -1
                    else:
                        self.output[i] = _input[i]
                    _input[i] = self.output[i]

            is_stable = True
            for i in range(pattern_length):
                if self.output[i] != _input[i]:
                    is_stable = False
            
            self.output = visualize(self.output, self.dim_x, self.dim_y, True)
            _input = copy.deepcopy(self.output)