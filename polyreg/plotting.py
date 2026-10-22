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
    return 0

def polyplots(x,y,n_values, future):
    "plots polynomial regression on data for given values of n in subplots"

    plt.scatter(x, y, color="black", label="Actual values") # plots original data points
    x_plot = np.asarray(x) 
    if future == True:
        x_plot = np.append(x_plot, [min(x) - 1, max(x) + 1])    # if future is True then it will predict two extra values either side of x: can be used to assess overfitting
    x_plot = np.sort(x_plot)
    for n in n_values:
        V = Vandermonde(x, len(x), n)  # to fit on the original data
        beta = optimal_coeff(V, y)
        V_plot = Vandermonde(x_plot, len(x_plot), n)
        y_pred = predictions(V_plot, beta) # gets predictions for original data AND two extra points IF future is True
        plt.plot(x_plot, y_pred, label=f"n={n} (degree {n-1})") # plots for the current degree of n

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Polynomial Regression for Different Degrees")
    plt.legend()
    plt.grid(True)
    plt.show()
    return 0