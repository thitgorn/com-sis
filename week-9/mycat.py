import ctypes

cat = ctypes.CDLL('./pipeCat.so')

cat.main('4300.txt')