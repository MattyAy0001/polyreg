import numpy as np
import matplotlib.pyplot as plt

def Vandermonde(x,m,n):
    "Gets the m by n+1 Vandermonde matrix for polynomial regression"
    V = np.ones((m,n+1)) # initialises the matrix
    for i in range(m):
        for j in range(1,n+1): # indexing starts from 1 as first column of V is already x^0=1
            V[i, j] = x[i] ** j # v(i,j) = (x[i])^j
    return V

def optimal_coeff(V,y):
    "Gets the optimal vector of coefficients according to a mean squared error loss function"
    return np.linalg.solve(V.T @ V, V.T @ y) # solves based on the normal equations

def predictions(x, y, beta, n):
    "Returns the preditions based on the optimal vector of coefficients beta"
    y_pred = Vandermonde(x, len(x), n) @ beta   # predictions are V @ beta
    return y_pred