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
    prevGuess = np.zeros((aRows, 1))
    for i in range (0, aRows):
        prevGuess[i,0] = 1000

#Establishes variables
    guess = np.zeros((aRows, 1))
    guess2 = np.zeros((aRows, 1))
    limit = 0
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])

#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((LA.norm(guess - prevGuess) > tol) and limit < 100):
        for j in range (0, aRows):
            guess2[j,0] = b[j,0]
            for i in range (0, aCols):
                if (i != j):
                  guess2[j,0] = guess2[j,0] -(A[j,i]) * (guess[j,0])
            guess2[j,0] = guess2[j,0] / A[j,j]
        prevGuess = guess
        guess = guess2
        guess2 = np.zeros((aCols, 1))
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





def gauss_seidel(file_name, tolIn):

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

#Sets initial previous guess so loop does not stop first try
    prevGuess = np.zeros((aRows, 1))
    for i in range (0, aRows):
        prevGuess[i,0] = 1000

    #Establishes variables
    guess = np.zeros((aRows, 1))
    guess2 = np.zeros((aRows, 1))
    limit = 0
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])
    runOnce = False


#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((LA.norm(guess - prevGuess) > tol) and limit < 100):
        if runOnce:
            prevGuess = guess
        for j in range (0, aRows):
            guess2[j,0] = b[j,0]
            for i in range (0, aCols):
                if (i != j):
                  guess2[j,0] = guess2[j,0] -(A[j,i]) * (guess[j,0])
            guess2[j,0] = guess2[j,0] / A[j,j]
            guess[j,0] = guess2[j,0]
        runOnce = True
        guess2 = np.zeros((aCols, 1))
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





jacobi("c.dat", 1e-10)
gauss_seidel("c.dat", 1e-10)

