import numpy as np
import sys
import pprint
from numpy import linalg as LA


def jacobi(file_name, tolIn):

    if file_name is None:
        exit()

#Turns file into one big matrix
    A = np.genfromtxt(file_name,delimiter=" ")
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])
    bdim = (aRows, 1)
    b = np.zeros(bdim)

#Creates nx1 b matrix
    for j in range(0, aRows):
       b[j,0] = A[j, aCols-1]


#Creates A matrix
    elim = [aCols-1]
    N = np.delete(A, elim, 1)
    A = N

    print(A)
    print ('\n')
    print(b)

#Sets tolerance
    tol = tolIn

#Sets intial previous guess so loop does not stop first try
    prevGuess = np.zeros((1, aRows))
    for i in range (0, aRows):
        prevGuess[0,i] = 1000

#Establishes variables
    guess = np.zeros((1, aRows))
    guess2 = np.zeros((1, aRows))
    limit = 0
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])

#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((np.linalg.norm(guess - prevGuess) > tol) and limit < 100):
        for j in range (0, aRows):
            guess2[0,j] = b[j,0]
            for i in range (0, aCols):
                if (i != j):

                    guess2[0,j] = guess2[0,j] -(A[j,i]) * (guess[0,i])
            guess2[0,j] = guess2[0,j] / A[j,j]

        for i in range(0, aCols):
                prevGuess[0,i] = guess[0,i]
        for i in range(0, aCols):
                guess[0,i] = guess2[0,i]
        guess2 = np.zeros((1, aCols))
        limit = limit + 1


    print ('\n')
    print(limit)
    print ('\n')
    print (guess)
    print ('\n')

    if limit >= 100:
        print("Did not converge after 100 iterations")
    else:
        print("Took " + str(limit) + " iterations to converge")
        return(limit)

#jacobi("c.dat", 1e-8)


