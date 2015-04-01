import random
import numpy as np
import sys

# Takes in a n value
def encode(n):
    n = int(n)
    xA0 = np.zeros((n+3,1))
    xA1 = np.zeros((n+3,1))
    xStream = np.zeros((n+3,1))

    # Creates a random x
    for i in range(0, n):
        xStream[i,0] = random.randint(0,1)

    # Creates A0 and A1 based on size
    xA0[0,0] = 1
    xA0[2,0] = 1
    xA0[3,0] = 1

    xA1[0,0] = 1
    xA1[1,0] = 1
    xA1[3,0] = 1

    A0 = np.zeros((n+3,n+3))
    A1 = np.zeros((n+3,n+3))
    y0 = np.zeros((n+3,1))
    y1 = np.zeros((n+3,1))
    yStream = []

    # Creates A0 and A1 using method defined in description
    for i in range(0,n+3):
        for k in range (0,i+1):
            A0[i,k] = xA0[i-k,0]
            A1[i,k] = xA1[i-k,0]

    # A0*x and A1*x to get y0 and y1
    for i in range(0,n+3):
        y0[i,0] = np.dot(A0[i,:], xStream)
        y1[i,0] = np.dot(A1[i,:], xStream)

    # Answers mod 2 to get real answers
    for i in range(0,n+3):
        y0[i,0] = y0[i,0]%2
        y1[i,0] = y1[i,0]%2

    # Combined for yStream
    for i in range(0,n+3):
        yStream.append([y0[i,0],y1[i,0]])

    print("x:")
    print(xStream)
    print("\n")
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
    print("yStream:")
    print(yStream)

    return xStream, A0, A1, y0, y1, yStream

# This is only or when encode is used as a stand-alone module
# Read command line argument. Must be exactly one argument.
# It outputs on the console
if __name__ == '__main__':
    xs, a0, a1, y0, y1, ys = encode(sys.argv[1])
    np.set_printoptions(precision=6, suppress=True)

    print("x:")
    print(xs)
    print("\n")
    print("A0:")
    print(a0)
    print("\n")
    print("A1:")
    print(a1)
    print("\n")
    print("y0:")
    print(y0)
    print("\n")
    print("y1:")
    print(y1)
    print("\n")
    print("yStream:")
    print(ys)