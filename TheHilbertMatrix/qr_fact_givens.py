# Author: Jenna Kwon

"""
QR factorization subroutine with Givens rotation
input: .dat file containing an input matrix A
Output: A, Q, R, error
"""

import numpy as np
import sys

# input : .dat file
# Output : Q, R and error |QR-A|inf


def qr_fact_givens(file_name):

    array = np.loadtxt(file_name)

    # Dimension, #row
    dims = array.shape
    n = dims[0]  # col
    m = dims[1]  # row

    if m != n:
        A = array[:, :-1]  # slice out the last column! called from solve_lu_b
        m -= 1
    else:
        A = array  # called from command line

    # Initialize R
    R = A

    # Place to store Gts for calculating Q
    listofGt = []

        # Calculate rotation matrices; cosine and sine move up/left
    # cos(theta) = a / sqrt(a + b), sin(theta) = -b / sqrt(a + b)
    for i in range(0, n):  # (0, 4) 0, 1, 2 column
        for j in range(m - 1, i, -1):  # row (1, 2, 3) (2, 3) (3)
            # print i, j
            G = np.identity(n, dtype='d')  # initialize rotation matrix
            c, s = generate_cos_sin(R[j - 1, i], R[j, i])
            # print c, s
            G[j, j] = c
            G[j, j - 1] = s
            G[j - 1, j] = -s
            G[j - 1, j - 1] = c
            Gt = np.transpose(G)
            listofGt.append(Gt)
            R = np.asmatrix(G) * np.asmatrix(R)

    # Initialize Q
    Q = np.identity(n, dtype='d')

    # Calculate Q
    for arr in listofGt:
        Q = np.asmatrix(Q) * np.asmatrix(arr)

    return A, Q, R, max(np.sum(np.asmatrix(Q)*np.asmatrix(R)-A, axis=1, dtype='d'))


def generate_cos_sin(a, b):
    r = np.sqrt(a*a + b*b)
    c = a / r
    s = -b / r
    return c, s


# This is only or when QR_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    A, Q, R, max_norm = qr_fact_givens(sys.argv[1])
    np.set_printoptions(precision=6, suppress=True)
    print 'A:'
    print A
    print '\nQ:'
    print Q
    print '\nR:'
    print R
    print '\nError:'
    print max_norm