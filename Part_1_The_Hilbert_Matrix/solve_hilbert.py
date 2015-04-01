# Author: Jenna Kwon
import numpy as np
import sys
import os
from lu_fact import lu_fact
from qr_fact_givens import qr_fact_givens
from qr_fact_househ import qr_fact_househ


def main():
    print '\nWelcome!'
    print 'By running this program, you have generated output_hilbert.txt file in your directory.'
    print 'I have solved "Hx = b" for you, for each n = 2,3, ..., 20 (size of H) and for b = 0.1/3(1, 1,...1)t.'
    print 'To view the file, type \'open output_hilbert.txt\''
    print 'Enjoy!\n'
    print 'WARNING: Some errors may be NaN due to precision issues'

    final_file = open('output_hilbert.txt', 'w')

    for i in range(2, 21):
        hilbert = generate_hilbert(i)
        dim = np.shape(hilbert)[0]
        b = 0.1**(dim/3.0) * np.ones((dim, 1))
        augmented = np.concatenate([hilbert, b], axis=1)
        file_name = 'hilbert_%s' % i
        temp = open(file_name, 'w')
        np.savetxt(file_name, augmented)
        try:
            A, L, U, error = lu_fact(file_name)
            final_file.write('--------------------------------------------------------------------')
            final_file.write('\nFor  n = %s ' % i)
            final_file.write('\nYour original matrix A: \n')
            np.savetxt(final_file, A, fmt='%1.5f')
            final_file.write('\nL: \n')
            np.savetxt(final_file, L, fmt='%1.5f')
            final_file.write('\nU: \n')
            np.savetxt(final_file, U, fmt='%1.5f')
            final_file.write('\nError for LU: ')
            final_file.write('%s\n' %error)

            A_scratch, Q, R, error_qr = qr_fact_givens(file_name)
            final_file.write('\nQ with givens: \n')
            np.savetxt(final_file, Q, fmt='%1.5f')
            final_file.write('\nR with givens: \n')
            np.savetxt(final_file, R, fmt='%1.5f')
            final_file.write('\nError for QR with givens: ')
            final_file.write('%s\n' %error_qr)


            A_scratch2, Qh, Rh, error_hh = qr_fact_househ(file_name)
            final_file.write('\nQ with householder: \n')
            np.savetxt(final_file, Q, fmt='%1.5f')
            final_file.write('\nR with householder: \n')
            np.savetxt(final_file, R, fmt='%1.5f')
            final_file.write('\nError for QR with househ: ')
            final_file.write('%s\n' %error_hh)

        finally:
            temp.close()
            os.remove(file_name)


def generate_hilbert(n):
    hilbert = np.zeros([n, n], dtype=np.float64)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            hilbert[i - 1, j - 1] = 1.0 / (i + j - 1.0)
    return hilbert


if __name__ == '__main__':
    main()