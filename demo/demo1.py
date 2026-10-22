# Demo file to demonstrate polyplots function
import numpy as np

from polyreg.plotting import polyplots

data = np.loadtxt("../data/SampleData.txt") # loads the sample data from the data folder located one folder up
x = data[:,0]
y = data[:,1]

n_values = [1,3,5,7,9] # different polynomials of 5 degrees
polyplots(x,y,n_values, future=False)   # first plot on the given (known) data
polyplots(x,y,n_values, future=True)    # then plot on the extra data, note the overfitting for higher powers of n