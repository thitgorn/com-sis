import numpy as np
import time

start = time.time()

x = 1000
y = 1000

file = open("DATA1000.dat","r")
arr = np.fromfile(file, dtype="float32")

for i in range(x):
    for j in range(y):
        z = arr[ (j*y) + i ]
        print z*z


end = time.time()
print(end - start)
