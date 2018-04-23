import ctypes

cat = ctypes.CDLL('./pipeGrep.so')

cat.main('4300.txt' , 'ant')