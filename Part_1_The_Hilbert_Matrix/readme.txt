<The Hilbert Matrix, Guide for Users>

I've included sample data in this directory for you
sample.dat file includes a 4x4 Hilbert matrix that you can use to test lu_fact.py, qr_fact_househ.py, and qr_fact_givens.py
sample2.dat file includes a 4x5 augmented matrix, [A|b], that you can use to test solve_lu_b.py, and solve_qr_b.py

!---------------!
1. (10 points) LU factorization, <lu_fact>
This is for when you want to get LU factorization of a square matrix, A. 
On your command line, run "python lu_fact.py arg1"
arg1 must be a .dat file containing a space-separated data of a N x N matrix, A.

It will output A, L, U, and ||LU − A||∞ on the console.

!---------------!
2. (20 points) QR factorization <qr_fact_househ, qr_fact_givens>
This is for when you want to get QR factorization of a square matrix, A. 
To get factorization of A with Householder transformation, run ”python qr_fact_househ.py arg1"
To get factorization of A with Givens rotation, "python qr_fact_givens arg1"
In both, arg1 must be a .dat file containing a space-separated data of a N x N matrix, A

It will output A, Q, R, and ||QR − A||∞ on the console.

!---------------!
3. (10 points) Solve Ax = b <solve_lu_b, solve_qr_b>
This is for when you want to solve a system, Ax = b.
To solve with LU factorization, run "python solve_lu_b.py arg1"
To solve with QR factorization, run ”python solve_qr_b.py qrg1 arg2”
With LU factorization, arg1 must be a .dat file containing a space-separated data of a N x (N + 1) augmented matrix [A|b]
With QR factorization, arg1 must be a .dat file containing a space-separated data of a N x (N + 1) augmented matrix [A|b]. Additionally, arg2 must be 0 or 1 (integer).
Inputting 0 will solve the system with Givens rotation, and 1 will solve the system with Householder transformation.

It will output A, solution vector xsol, and the norm ||Axsol − b||.

!---------------!
4. (10 points) Solutions and Errors for Hilbert Matrix
This is for when you want to solve a system, Hx = b, where H(n x n) is a Hilbert matrix and b is a vector, b = 0.1/3(1, 1,…1)t for n = 2, 3, … 20. 
To see the results, run "python solve_hilbert.py"

This will produce output.txt containing H, L, U, Error for LU, Q, R, Error for QR (givens),Q, R, Error for QR (householder), for each n = 2, 3, .. 20.
There is no need to input any data. H will be generated for you.

!---------------!
5. (10 points) Plots and discussion
Please see part1_written.docx
It includes plots of the errors obtained for the Hilbert matrix as a function of n.
There are three plots for the errors of Xsol: one for ||LU − H||∞, and two more
for ||QR − H||∞ (givens and householder).
The discussion should address the questions posted in the description of the project.

