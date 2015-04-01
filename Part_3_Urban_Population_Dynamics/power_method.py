# Author = Vivienne Qie

"""
Power method iteration
Input: .dat file containing an input matrix A, error tolerance, and initial approximation vector u0
Output: approx. eigenvalue, approx. eigenvector v, number of iterations
"""

import numpy as np
import sys
from numpy import linalg as LA


def power_method(file_name, error_tol, u0):

    # Creates a matrix from the .dat file
    A = np.genfromtxt(file_name, delimiter=" ")

    m = int(A.shape[0]) #rows of A

    u = np.asarray(np.asmatrix(u0))
    uRows = int(u.shape[0]) #rows of u
    uCols = int(u.shape[1]) #columns of u

    # Sets the tolerance
    tol = error_tol

    # Sets the initial number of iterations
    iteration = 0

    # Sets an array with one entry 0 to use for the error in the while loop
    eigenvalues = [0]

    # While number of iterations is less than 100, the matrix
    # A is raised to a power equal to the iteration and multiplied
    # by the original u0 that was given as an input. The dominant
    # eigenvector is found and from that, the dominant eigenvalue
    # is found.
    while iteration < 100:
        copyA = LA.matrix_power(A, iteration+1)
        x = np.zeros(shape=(m, uCols))
        for i in range(m):
            for j in range(uCols):
                for k in range(uRows):
                    x[i][j] += (copyA[i][k] * u[k][j]) #Multiplies matrix A and u
        eigenvector = x / LA.norm(x) # Finds the dominant eigenvector
        eigenRows = int(eigenvector.shape[0]) #rows of dominant eigenvector
        eigenCols = int(eigenvector.shape[1]) #columns of eigenvector

        Ax = np.zeros(shape = (m, eigenCols))

        for i in range(m):
            for j in range(eigenCols):
                for k in range(eigenRows):
                    Ax[i][j] += A[i][k] * eigenvector[k][j]
        Axx = np.vdot(Ax, eigenvector)
        xx = np.vdot(eigenvector, eigenvector)
        eigenvalue = Axx / xx # Finds the dominant eigenvalue

        eigenvalues.append(eigenvalue)

        if (np.absolute(eigenvalues[iteration+1] - eigenvalues[iteration])) <= tol:
            break

        iteration += 1

    print "Dominant eigenvalue = ", eigenvalue
    print "Dominant eigenvector =\n", eigenvector

    if iteration >= 100:
        print "Did not converge after 100 iterations."
    else:
        print "Took " + str(iteration) + " iterations to converge."


# This is only for when power_method is used as a stand-alone module
# Reads command line arguments. Must be exactly three arguments
# It outputs on the console
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print '\nWrong input format!'
        print 'Please input filename as your first argument'
        print 'Please enter a float representing error tolerance as your second argument'
        print 'Please enter a eigenvector as your third argument as a string'
    else:
        power_method(sys.argv[1], sys.argv[2], sys.argv[3])