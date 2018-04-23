import os, os.path
import threading
import sys

count = 1

class Counter(threading.Thread):
    def __init__(self,dirname):
        threading.Thread.__init__(self)
        self.dirname = dirname

    def countdir(self,dirname):
        if (os.path.isdir(dirname)):
            global count
            count = count+1

        fileList = os.listdir(dirname)
        dir = []
        for file in fileList:
            filename = dirname + "/" + file
            if (os.path.isdir(filename)):
                dir.append(Counter(filename))

        for d in dir:
            d.start()
        for d in dir:
            d.join()
    
    def run(self):
        self.countdir(self.dirname)

def main(dir):
    countdir = Counter("." + dir)
    countdir.start()

    countdir.join()
    print (count)

if __name__ == '__main__':
    main(sys.argv[1])