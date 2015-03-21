# Author: Jenna Kwon
import numpy as np
import sys
import pprint

# input : .dat file
# Output :  L, U, and error |LU-A|inf


def lu_fact(file_name):

    if file_name is None:
        exit()

    # A = ndarray
    A = np.loadtxt(file_name, unpack=True)

    # Dimension
    n = A.shape[0]

    # Initialize L & U.
    # L = I, U = A for Doolittle algorithm
    L = np.identity(n, dtype='d')
    U = A

    # LU fact without partial pivoting
    # Doolittle algorithm is used
    # Assumes that factorization exists
    # Aij = sum of Lip*Upj, p = counter
    # Fill in L below the diagonal
    # Lij = (aij - sum of lip * upj) / ujj. i > j
    # Uij = (aij - sum of lip  * upj).
    # Fill in U above the diagonal
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] = U[j, i:] - L[j, i] * U[i, i:]
            U[j, i] = 0

    print A, L, U


# For when lu_fact is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
if __name__ == '__main__':
    lu_fact(sys.argv[1])
# else:
#     #do nothing