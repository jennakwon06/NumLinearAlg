# Author: Jenna Kwon

"""
Calls lu_fact to obtain the solution to a system Ax = b.
input: .dat file containing an augmented matrix A|b
Output: x(sol)
"""

import numpy as np
import sys
from lu_fact import lu_fact


def solve_lu_b(file_name):

    # get matrices and error from lu_fact
    A, L, U, error = lu_fact(file_name)
    np.set_printoptions(precision=6, suppress=True)

    # isolate b
    augmented = np.loadtxt(file_name)
    n = augmented.shape[0]
    b = augmented[:, n]

    # Implement forward-backward substitution
    # LUx = B
    # First, solve Ly = b
    # Then, solve Ux = y

    # SOLVING LY = B, Y = L-1*B. FORWARD SUBSTITUTION
    y = np.zeros((n, 1))
    for i in range(0, n):
        y[i] = b[i]  #
        for j in range(0, i):
            y[i] = y[i] - L[i, j] * y[j]
        y[i] = y[i] / L[i, i]

    # SOLVING UX = Y, X = U-1*Y. BACKWARD SUBSTITUTION
    x = np.zeros((n, 1))
    for p in range(n - 1, -1, -1):
        x[p] = y[p]
        for q in range(p + 1, n):
            x[p] = x[p] - U[p, q] * x[q]
        x[p] = x[p] / U[p, p]

    error_final = np.linalg.norm(np.asmatrix(A)*np.asmatrix(x) - b)

    return x, error_final

# This is only or when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the consoorle
if __name__ == '__main__':
    solution, error = solve_lu_b(sys.argv[1])
    np.set_printoptions(precision=6, suppress=True)
    print 'Xsol:'
    print solution
    print '\nError ||Ax(sol) - B||: '
    print error