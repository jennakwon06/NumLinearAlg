# Author: Jenna Kwon

"""
LU factorization subroutine
input: .dat file containing an input matrix A
Output: A, L, U, error
"""

import numpy as np
import sys
import os

# Subroutine to output A, L, U, and error by taking in input file from cmd line
def lu_fact(file_name):

    array = np.loadtxt(file_name)

    # Dimension, #row
    dims = array.shape
    n = dims[0]  # row
    m = dims[1]  # col

    if m != n:
        A = array[:, :-1]  # slice out the last column! called from solve_lu_b
        m -= 1
    else:
        A = array  # called from command line

    # Initialize L & U as L = I, U = A for Doolittle algorithm
    L = np.identity(n, dtype='d')
    U = A

    # LU fact without partial pivoting
    # Pseudo code was referred from a cited source below:
    # "LU factorization: Lecture 20 in "Numerical Linear Algebra" by Trefethen and Bau, SIAM, Philadelphia, 1997"
    #
    # This algorithm assumes that factorization exists
    # Idea is to introduce 0s in U below the diagonal and to fill in L
    # Fill in U above the diagonal
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:n] = U[j, i:] - (L[j, i] * U[i, i:n])

    # Error, max norm, is defined as the maximum sum of the absolute values of each row
    error = max(np.sum(abs(np.asmatrix(L)*np.asmatrix(U)-A), axis=1, dtype='d'))

    return A, L, U, error

# This is only or when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    A, L, U, max_norm = lu_fact(sys.argv[1])
    np.set_printoptions(precision=6, suppress=True)
    print 'Your original matrix A:'
    print A
    print '\nL solved with LU factorization:'
    print L
    print '\nU solved with LU factorization:'
    print U
    np.set_printoptions(precision=15, suppress=False)
    print '\nError ||LU-A||inf:'
    print max_norm
    print '\n'