# Author: Jenna Kwon

"""
QR factorization subroutine with Householder rotation
input: .dat file containing an input matrix A
Output: A, Q, R, error
"""

import numpy as np
import sys
import copy

# input : .dat file
# Output : Q, R and error |QR-A|inf


def qr_fact_househ(file_name):

    array = np.loadtxt(file_name)

    # Dimension, #row
    dims = array.shape
    n = dims[0]  # col
    m = dims[1]  # row

    if m != n:
        A = array[:, :-1]  # slice out the last column! called from solve_lu_b
    else:
        A = array  # called from command line

    # Initialize R
    R = copy.copy(A)

    # Place to store Gts for calculating Q
    listofH = []

    for i in range(0, n):
        H_initial = np.identity(n, dtype='d')
        I = np.identity(n - i, dtype='d')
        Rtemp = copy.copy(R)
        v = Rtemp[i:, i:i+1]
        v[0] = v[0] - np.linalg.norm(v)
        ui = v / np.linalg.norm(v)
        H_initial[i:, i:] = I - (2 * np.asmatrix(ui) * np.asmatrix(np.transpose(ui)))
        listofH.append(H_initial)
        R =  np.asmatrix(H_initial) * np.asmatrix(R)

    # Initialize Q
    Q = np.identity(n, dtype='d')

    # Calculate Q
    for arr in listofH:
        Q = np.asmatrix(Q) * np.asmatrix(arr)

    return A, Q, R, max(np.sum(Q*R-A, axis=1, dtype='d'))


# This is only or when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the consoorle
if __name__ == '__main__':
    A, Q, R, max_norm = qr_fact_househ(sys.argv[1])
    np.set_printoptions(precision=6, suppress=True)
    print 'A:'
    print A
    print '\nQ:'
    print Q
    print '\nR:'
    print R
    print '\nError:'
    print max_norm