# Author: Jenna Kwon

"""
Calls qr_fact_givens or qr_fact_househ to obtain the solution to a system Ax = b.
input: .dat file containing an augmented matrix A|b
Output: x(sol)
"""

import numpy as np
import sys
from qr_fact_givens import qr_fact_givens
from qr_fact_househ import qr_fact_househ


def solve_qr_b(argv):

    # guard against null argument
    if argv is None or len(argv) > 2:
        print 'Please put filename as your first argument.'
        print 'Your second argument should be an integer of 0 or 1'
        print 'Use 0 if you would like to use givens rotation'
        print 'Use 1 if you would like to use householders transformation'
        exit(1)

    if argv[1] == 0:
        print 'Using Givens rotation: '
        A, Q, R, error = qr_fact_givens(argv[0])
    else:
        print 'Using Householder transformation: '
        A, Q, R, error = qr_fact_househ(argv[0])

    # set print options
    np.set_printoptions(precision=6, suppress=True)

    # isolate b
    augmented = np.loadtxt(argv[0])
    n = augmented.shape[0]
    b = augmented[:, n]
    b = np.reshape(b, (4, 1))

    # Rx = QtB is a two step process
    # One: d = QtB is a simple calculation
    # Two: Solve Rx = d by back substitition

    # One
    d = (np.transpose(Q)) * b

    # Two
    x = np.zeros((n, 1))
    for p in range(n - 1, -1, -1):
        x[p] = d[p]
        for q in range(p + 1, n):
            x[p] = x[p] - R[p, q] * x[q]
        x[p] = x[p] / R[p, p]

    error_final = np.linalg.norm(np.asmatrix(A)*np.asmatrix(x) - b)

    return x, error_final

# This is only or when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    solution, error = solve_qr_b(sys.argv[1:])
    np.set_printoptions(precision=6, suppress=True)
    print 'Xsol: '
    print solution
    print '\nError ||Ax(sol) - B||: '
    print error