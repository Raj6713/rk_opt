import numpy as np
import pandas as pd
from src.helper_function import  calculate_enter_and_exit

class Simplex(object):
    """
    Simplex method class:
    Return the table of the solved simplex method and also saves the csv.
    # Input format:
    xi: encode the values in this format for the variables:
    yi: encode balancing variable in this format
    Z: This variable is to encode minimizatio/maximization function.
    C: Cost function.
    x1,   x2,   y1,   y2,   Z,   C
    1,    1,    1,    0,    0,   12
    2,    1,    0,    1,    0,   16
   -40,   -30,  0,    0,    1,    0

    """
    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv
        self.problem_frame = pd.read_csv(self.path_to_csv)

    def iteration(self):
        optimization_row = self.problem_frame.tail(1)
        index_value = self.problem_frame.tail(1).index.values.astype(int)[0]
        optimization_transform = optimization_row.T
        # print(optimization_transform)
        minimum_value = np.min(optimization_transform[index_value])
        variable_name = optimization_transform[optimization_transform[index_value] == minimum_value].index.values[0]
        calculate_enter_and_exit(self.problem_frame, minimum_value, variable_name, index_value)







