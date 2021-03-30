import numpy as np
import sys
from Equation import Expression


class NewtonRaphson(object):
    """
    Class based program to find root of a equation using newton raphson method.
    equation: string in format of x^2+x+1=0
    """
    def __init__(self, equation, range_arg):
        self.range_arg = range_arg
        self.lower_limit, self.upper_limit = map(float, self.range_arg[1:-1].strip().split(","))
        self.equation = equation
        value_range = np.linspace(self.lower_limit, self.upper_limit, 20)
        self.dictionary = dict()
        for i in range(len(value_range)-1):
            # print(value_range[i], value_range[i+1])
            if self.create_functional_equivalent(value_range[i]) * self.create_functional_equivalent(value_range[i+1]) <= 0:
                self.dictionary[value_range[i]] = "change"

    def create_functional_equivalent(self, value):
        functional_expression = Expression(self.equation, ["x"])
        return functional_expression(value)

    def derivative_for_function(self, value):
        h = 0.00001
        diff_fx = self.create_functional_equivalent(value+h)-self.create_functional_equivalent(value)
        diff_fx = diff_fx/h
        return diff_fx

    def evaluate(self):
        eps = 0.00001
        i = 0
        for key, value in self.dictionary.items():
            error = np.inf
            initial_root = key
            while error > eps:
                new_root = initial_root - (self.create_functional_equivalent(initial_root) /
                                           self.derivative_for_function(initial_root))
                error = abs(new_root - initial_root)
                initial_root = new_root
            print("Root_{0} is: {1} ".format(i, initial_root))
            i += 1


if __name__ == "__main__":
    equation_from_str = sys.argv[1]
    range_argument = sys.argv[2]
    problem = NewtonRaphson(equation_from_str, range_argument)
    problem.evaluate()
