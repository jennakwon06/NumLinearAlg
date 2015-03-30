import random
import numpy as np
import sys
import pprint
from numpy import linalg as LA

#Takes in a n value
def encode(n):
#Creates a random x (and X vector to help define A1)
    x = np.zeros((1,n+3))
    xA1 = np.zeros((1,n+3))

    for i in range(0, n):
        x[0,i] = random.randint(0,1)

    for i in range(0, n+3):
        xA1[0,i] = x[0,i]

    xA1[0,1] = x[0,2]
    xA1[0,2] = x[0,1]
    x = np.matrix(([1], [0], [1], [1], [0], [0], [0], [0]))
    xA1 = np.matrix(([1], [1], [0], [1], [0], [0], [0], [0]))
    A0 = np.zeros((n+3,n+3))
    A1 = np.zeros((n+3,n+3))
    y0 = np.zeros((n+3,1))
    y1 = np.zeros((n+3,1))
    yStream = []

#Creates A0 and A1 using method defined in description
    for i in range(0,n+3):
        for k in range (0,i+1):
            A0[i,k] = x[i-k,0]
            A1[i,k] = xA1[i-k,0]

#A0*x and A1*x to get y0 and y1
    for i in range(0,n+3):
        y0[i,0] = np.dot(A0[i,:], x)
        y1[i,0] = np.dot(A1[i,:], x)

#answers mod 2 to get real answers
    for i in range(0,n+3):
        y0[i,0] = y0[i,0]%2
        y1[i,0] = y1[i,0]%2

#combined for yStream
    for i in range(0,n+3):
        yStream.append([y0[i,0],y1[i,0]])

    print("x:")
    print(x)
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






encode(5)