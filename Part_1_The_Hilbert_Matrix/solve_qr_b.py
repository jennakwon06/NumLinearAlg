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

    if argv[1] == 0:
        print '\nUsing Givens rotation: '
        A, Q, R, error = qr_fact_givens(argv[0])
    else:
        print '\nUsing Householder transformation: '
        A, Q, R, error = qr_fact_househ(argv[0])

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

    # Output ||Ax - b||
    norm_final = np.linalg.norm(np.asmatrix(A)*np.asmatrix(x) - b)

    return A, b, x, norm_final

# This is only or when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '\nWrong input format!'
        print 'Please input filename as your first argument'
        print 'Please input 0 or 1 as your second argument to specify your preferred factorization'
        print '0 = Givens rotation'
        print '1 = Householder transformation\n'
    else:
        A, b, solution, norm = solve_qr_b(sys.argv[1:])
        np.set_printoptions(precision=6, suppress=True)
        print 'Your original matrix A:'
        print A
        print '\nYour original vector b:'
        print b
        print '\nXsol:'
        print solution
        print '\n||Ax(sol) - B||: '
        print norm
        print '\n'