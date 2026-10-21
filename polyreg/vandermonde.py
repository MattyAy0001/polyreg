import numpy as np

def Vandermonde(x,m,n):
    "Gets the m by n+1 Vandermonde matrix for polynomial regression"
    V = np.ones((m,n+1)) # initialises the matrix
    for i in range(m):
        for j in range(1,n+1): # indexing starts from 1 as first column of V is already x^0=1
            V[i, j] = x[i] ** j
            print(V[i,j])
    return V

def optimal_coeff(V,y):
    "Gets the optimal matrix of coefficients according to a mean squared error loss function"
    return np.linalg.solve(V.T @ V, V.T @ y) # solves based on the normal equations

