import matplotlib.pyplot as plt
import numpy as np
from polyreg.vandermonde import Vandermonde, optimal_coeff, predictions

def plot(x,y):
    "takes two vectors as inputs and plots them against each other"
    plt.figure()
    plt.plot(x,y,'.')
    plt.title("Graph of x against y")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    plt.show()
    return None