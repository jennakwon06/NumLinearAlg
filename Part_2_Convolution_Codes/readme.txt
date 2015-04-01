<The Convolution Codes, Guide for Users>

!---------------!
1. (4 points) Encoding Problem

How to Run:
To run, type "python Encode.py arg1" in the command line

Input specification:
this program takes in a single value arg1
arg1: should be a single integer n (cannot be less than 4) value. Example, 4

Outputs:
The script produces an x vector, A0 matrix, A1 matrix, y0 vector, y1 vector, and yStream

!---------------!
2. (12 points) Jacobi/Gauss-Seidel Iterative Methods

How to Run:
There are two iterative method functions
-To run the Jacobi function you must type in "python Jacobi.py arg1 arg2" in the command line.
-To run the Gauss_Seidel function you mus type in "python Gauss_Seidel.py arg1 arg2" into the command line.

Input specification:
arg1: The filename of the dat file containing an augmented matrix of size (N X (N+1), [A|b]. Example: b.dat
arg2: tolerance thershold of type float. Example: 1e-8
When run, program will ask for the user input to get an initial guess vector.
This vector's length must be equal to the amount of rows of the matrix in .dat file
Vector should be separated by zeroes. Example: 1 5 2 8 (if there are 4 rows in the matrix)

Outputs:
This script reports the number of iterations and the final answer.
The method will stop the iterations if the matrix did not converge after 100 iterations.

!---------------!
2. (4 points) Decoding

How to Run:
To run the Decoding function you must type in "python Decode.py" into the command line.

Inputs:
Running the program will prompt the user to enter the y0 and y1 of the y stream (length cannot be less than 4).
Enter both streams, separating values by spaces. Example: 1 0 0 0 1 0 1 0

Outputs:

There are two functions that both take a single yStream (whose length cannot be less than 4). One uses the Jacobi iteraitve method, and one uses Gauss-Seidel. The code will create an A0 and A1 based on n and iterate it to return an xStream. It will print the inputs, the x stream, and the number iterations it took with the jacobi method and the gauss_seidel method.