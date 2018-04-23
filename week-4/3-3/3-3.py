import ctypes
import numpy as np
import time

def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 :
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

start = time.time()
row = 10000
col = 10000
filename = "./DATA10000.dat"

testlib = ctypes.CDLL('./3-3.so')
testlib.setUp(filename,row,col)
testlib.next.restype = ctypes.c_float

run = 0
array = np.empty((row,col))
while(testlib.hasNext()):
    array[run%col][run%row] = (testlib.next())
    run = run+1

print("finish created array")
matmult(array,array)

end = time.time()
print(end - start)
