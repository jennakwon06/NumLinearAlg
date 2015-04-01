# Author = Vivienne Qie

"""
Iteration to find population of a certain decade
Input: .dat file containing an input matrix A, initial approximation vector u0,
    and number of decades to go ahead
Output: vector of population distribution, total population
"""

import numpy as np
import sys
from numpy import linalg as LA

def population(file_name, u0, decades):

    # Creates a matrix from the .dat file
    A = np.genfromtxt(file_name, delimiter=" ")

    m = int(A.shape[0]) #rows of A

    u = np.matrix(u0)
    uCols = int(u.shape[1]) #columns of u

    # Sets the initial number of iterations
    iteration = 0

    # Raises matrix A to power decades and multiplies the resulting matrix
    # by the initial approximation vector (population in 2000)
    while iteration < decades:
        copyA = LA.matrix_power(A, iteration+1)
        x = np.zeros(shape = (m, uCols))
        x = np.dot(copyA, u0)
        iteration += 1

    # Sets initial total population
    total_pop = 0

    # Adds every entry in vector x to find total population
    for i in range(len(x)):
        total_pop += x[i]

    print "Population distribution:\n", x
    print "Total population: ", total_pop

# This is only for when population is used as a stand-alone module
# Reads command line arguments. Must be exactly three arguments
# It outputs on the console
if __name__ == "__main__":
    population(sys.argv[1], sys.argv[2], sys.argv[3])
