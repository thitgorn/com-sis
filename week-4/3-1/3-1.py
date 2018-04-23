import ctypes
import time

start = time.time()

testlib = ctypes.CDLL('./3-1.so')
testlib.multiplication('./DATA1000.dat',1000,1000)

end = time.time()
print(end - start)
