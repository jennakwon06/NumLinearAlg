import random
import numpy as np
import sys
import pprint
from numpy import linalg as LA

def decode():
    s = raw_input("Please provide list of your y0 values separated by spaces, e.g. 1 2 3: ")
    y0 = np.matrix(s)
    s = raw_input("Please provide list of your y1 values separated by spaces, e.g. 1 2 3: ")
    y1 = np.matrix(s)
    s = raw_input("Please provide list of your guess values (equal to number of rows) separated by spaces, e.g. 1 2 3: ")
    guess = np.matrix(s)
    guess3 = np.matrix(s)
    x = y0.shape
    n = (x[1])

    yStream = []

    for x in y0:
        yStream.append([y0[0,x], y1[0,x]])

    print("\n")
    print("yStream")
    print(yStream)
    print("\n")

    y0 = y0.transpose()
    y1 = y1.transpose()

    xA0 = np.zeros((n,1))
    xA1 = np.zeros((n,1))

    #Creates A0 and A1 based on size
    xA0[0,0] = 1
    xA0[2,0] = 1
    xA0[3,0] = 1

    xA1[0,0] = 1
    xA1[1,0] = 1
    xA1[3,0] = 1

    A0 = np.zeros((n,n))
    A1 = np.zeros((n,n))

    #Creates A0 and A1 using method defined in description
    for i in range(0,n):
        for k in range (0,i+1):
            A0[i,k] = xA0[i-k,0]
            A1[i,k] = xA1[i-k,0]

    print("A0:")
    print(A0)
    print("\n")
    print("A1:")
    print(A1)
    print("\n")
    print("y0:")
    print(y0)
    print("\n")
    print("y1:")
    print(y1)
    print("\n")



    aRows = int(A0.shape[0])
    aCols = int(A0.shape[1])
#### Implements code from Jacobi Method###
#Sets tolerance
    tol = 1e-8

#Sets intial previous guess so loop does not stop first try
    prevGuess = np.zeros((1, aRows))
    for i in range (0, aRows):
        prevGuess[0,i] = 1000

#Establishes variables
    guess2 = np.zeros((1, aRows))
    limit = 0


#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((np.linalg.norm(guess - prevGuess) > tol) and limit < 100):
        for j in range (0, aRows):
            guess2[0,j] = y0[j, 0]
            for i in range (0, aCols):
                if (i != j):

                    guess2[0,j] = guess2[0,j] -(A0[j,i]) * (guess[0,i])
            guess2[0,j] = guess2[0,j] / A0[j,j]

        for i in range(0, aCols):
                prevGuess[0,i] = guess[0,i]
        for i in range(0, aCols):
                guess[0,i] = guess2[0,i]
        guess2 = np.zeros((1, aCols))
        limit = limit + 1

    x = guess.shape
    length = x[1]
    xStream = []


    for i in range(0, length):
        xStream.append(abs(guess[0, i])%2)

####^^^ Implements code from Jacobi Method ^^^###

#### Implements code from Gauss-Seidel Method###

#Sets initial previous guess so loop does not stop first try
    prevGuess2 = np.zeros((1, aRows))
    for i in range (0, aRows):
        prevGuess2[0,i] = 1000

    #Establishes variables
    guess4 = np.zeros((1, aRows))
    limit2 = 0
    aRows = int(A0.shape[0])
    aCols = int(A0.shape[1])
    runOnce = False


#Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
#reached.
    while ((np.linalg.norm(guess3 - prevGuess2) > tol) and limit2 < 100):

        if runOnce:
            for i in range(0, aCols):
                prevGuess2[0,i] = guess3[0,i]
        for j in range (0, aRows):
            guess4[0,j] = y0[j,0]
            for i in range (0, aCols):
                if (i != j):
                  guess4[0,j] = guess4[0,j] -(A0[j,i]) * (guess3[0,i])
            guess4[0,j] = guess4[0,j] / A0[j,j]
            guess3[0,j] = guess4[0,j]


        runOnce = True
        guess4 = np.zeros((1, aRows))
        limit2 = limit2 + 1


####^^^ Implements code from Jacobi Method ^^^###

    if limit >= 100:
        statement = ("Did not converge after 100 iterations")
        return statement
    else:
        statement = ("Took " + str(limit) + " iterations to converge using Jacobi Method")
        statement2 = ("Took " + str(limit2) + " iterations to converge using Gauss Seidel Method")
        return limit, limit2, guess, statement, statement2

    print ('\n')
    print("Jacobi iterations:")
    print(limit)
    print ('\n')
    print("Gauss-Seidel iterations:")
    print(limit2)
    print ('\n')
    print("x Stream:")
    print (xStream)
    print ('\n')


# This is only or when gauss_seidel is used as a stand-alone module
# Read command line argument. Takes no inputs.
# It outputs on the console
if __name__ == '__main__':
    limit, limit2, xStream, statement, statement2 = decode()
    np.set_printoptions(precision=6, suppress=True)


     print ('\n')
    print (xStream)
    print ('\n')
    print(statement)
    print ('\n')
    print(statement2)

#decode()
