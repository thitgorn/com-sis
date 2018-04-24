from multiprocessing import Queue
import threading
import struct
import sys

multi_results = Queue()

def readDataIntoQueue(filename , data_queue):
    f = open(filename, "rb")
    try:
        byte = f.read(4)
        datas = []
        while byte:
            number = struct.unpack("<L", byte)[0]
            datas.append(number)
            byte = f.read(4)

        count = 0
        arrs = []
        for d in datas:
            arrs.append(d)
            if(len(arrs)==4):
                # print(arrs)
                data_queue.put(arrs)
                arrs = []
    finally:
        f.close()

class Multiplication(threading.Thread):
    def __init__(self,dataQueue):
        threading.Thread.__init__(self)
        self.dataQueue = dataQueue
    
    def multiply(self):
        global multi_results
        while 1:
            if self.dataQueue.empty():
                break
            datas = self.dataQueue.get()
            # print datas
            for x in range(0,len(datas)):
                mul = datas[x] * datas[x]
                multi_results.put(mul)

    def run(self):
        self.multiply()

class Sumation(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def sum(self):
        global multi_results
        while 1:
            datas = []
            for x in range(0, 3):
                data = multi_results.get()
                datas.append(data)
                if multi_results.empty():
                    break
            sum = 0
            for x in range(0, len(datas)):
                sum = sum + datas[x]
            if multi_results.empty():
                multi_results.put(sum)
                print multi_results.get()
                break
            else:
                multi_results.put(sum)

    def run(self):
        self.sum()

def main(filename):
    data_queue = Queue()
    readDataIntoQueue(filename,data_queue)
    for x in range(0,3):
        Multiplication(data_queue).run()
    for x in range(0,3):
        Sumation().run()

if __name__ == '__main__':
    main(sys.argv[1])