import numpy as np
import sys
from src.simplex_method import Simplex

if __name__ == '__main__':
    file_path = sys.argv[1]
    # print(Simplex.__doc__)
    simplex = Simplex(file_path)
    simplex.iteration()

