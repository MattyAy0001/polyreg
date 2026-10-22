# Demo file to show off functions in vandermonde.py
import numpy as np
from polyreg.vandermonde import Vandermonde, optimal_coeff, predictions, avg_loss

data = np.loadtxt("../data/SampleData.txt") # loads the sample data from the data folder located one folder up
x_data = data[:,0]
y_data = data[:,1]

n = 5   # polynomial of degree 5

Vander = Vandermonde(x_data, len(x_data), n)
print("Vandermonde matrix:")
print(Vander)
print("Dimensions of the matrix:")
print(np.shape(Vander))

Beta = optimal_coeff(V=Vander, y=y_data)
print("Optimal coefficient vector beta:")
print(Beta)

y_predicted = predictions(V=Vander, beta=Beta)
print("Prediction vector for y:")
print(y_predicted)

average_loss = avg_loss(y=y_data, y_pred=y_predicted)
print("Average loss for the data:")
print(average_loss)
