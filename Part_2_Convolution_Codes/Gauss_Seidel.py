import numpy as np
import sys

def gauss_seidel(file_name, tolIn):

    # Turns file into one big matrix
    A = np.genfromtxt(file_name,delimiter=" ")
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])
    bdim = (aRows, 1)
    b = np.zeros(bdim)

    s = raw_input("Please provide list of your guess values separated by spaces, e.g. 1 2 3: ")
    guess = np.matrix(s)

    # Creates nx1 b matrix
    for j in range(0, aRows):
       b[j,0] = A[j, aCols-1]

    # Creates A matrix
    elim = [aCols-1]
    N = np.delete(A, elim, 1)
    A = N

    print ('\nYour input matrix A')
    print(A)
    print ('\nYour input vector b')
    print(b)

    #Sets tolerance
    tol = float(tolIn)

    #Sets initial previous guess so loop does not stop first try
    prevGuess = np.zeros((1, aRows))
    for i in range (0, aRows):
        prevGuess[0,i] = 1000

    #Establishes variables
    guess2 = np.zeros((1, aRows))
    limit = 0
    aRows = int(A.shape[0])
    aCols = int(A.shape[1])
    runOnce = False


    #Runs while the norm of the (previous guess vector - the current guess) is less than the tolerance or max iterations are
    #reached
    while (np.linalg.norm(guess - prevGuess) > tol) and limit < 100:

        if runOnce:
            for i in range(0, aCols):
                prevGuess[0,i] = guess[0,i]
        for j in range (0, aRows):
            guess2[0,j] = b[j,0]
            for i in range (0, aCols):
                if (i != j):
                  guess2[0,j] = guess2[0,j] -(A[j,i]) * (guess[0,i])
            guess2[0,j] = guess2[0,j] / A[j,j]
            guess[0,j] = guess2[0,j]

        runOnce = True
        guess2 = np.zeros((1, aRows))
        limit = limit + 1

    if limit >= 100:
        statem = "Did not converge after 100 iterations"
        limit = "INVALID"
        guess = "INVALID"
        return limit, guess, statem
    else:
        statement = str(limit)
        return limit, guess, statement

# This is only or when gauss_seidel is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    limit, guess, statement = gauss_seidel(sys.argv[1], sys.argv[2])
    print ('\nLimit:')
    print(limit)
    print ('\nGuess: ')
    print (guess)
    print ('\nNumber of iterations took to converge:')
    print(statement)
    print ('\n')