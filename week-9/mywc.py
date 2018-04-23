import ctypes

cat = ctypes.CDLL('./pipeWc.so')

cat.main('4300.txt' , 'ant')