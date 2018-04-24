import struct
import sys

def main(filename):
    f = open(filename, "rb")
    sum = 0
    try:
        byte = f.read(4)
        while byte:
            number = struct.unpack("<L", byte)[0]
            number = number * number
            sum = sum + number
            byte = f.read(4)
    finally:
        f.close()
    print ("sum = " , sum)

if __name__ == '__main__':
    main(sys.argv[1])
