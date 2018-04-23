from ctypes import *
import numpy as np
import time


def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 :
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def readBinaryByC():
    cprogram = CDLL('./q1.so')
    cprogram.binaryToArray()
    cprogram.nextBinaryArray.restype = c_float
    array = np.empty((1000,1000))

    count = 0
    for row in range(0,1000):
        for col in range(0,1000):
            test = cprogram.nextBinaryArray()
            array[row][col] = test
    return array

start = time.time()
array = readBinaryByC()
res = matmult(array,array)
end = time.time()
print(end-start)
