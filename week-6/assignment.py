import threading
import random
import time
import logging

M=100000
N=100000

def withdraw(fromAcc,fromAcc2):
    t_withdraw = 0
    for i in (range(M)):
        r = random.random()
        logging.debug('Sleeping %0.02f', r)
        # time.sleep(r)
        fromAcc.withdraw(r)
        fromAcc2.withdraw(r)
        t_withdraw -= r
 #print how much you subtract from and new acc value
    print ('withdraw = ' , t_withdraw)

def deposit(toAcc,toAcc2):
    t_deposit = 0
    for i in (range(50)):
        r = random.random()
        logging.debug('Sleeping %0.02f', r)
        # time.sleep(r)
        toAcc.deposit(r)
        toAcc2.deposit(r)
        t_deposit += r
        # print how much you add and  new acc value
    print ('deposit = ' , t_deposit)

class bankAcc(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start  # initial account value

    def withdraw(self,value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            temp = self.value
            logging.debug('Acquired a lock')
            temp -= value
            self.value = temp
        finally:
            logging.debug('released a lock')
            self.lock.release()


    def deposit(self,value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            temp = self.value
            logging.debug('Acquired a lock')
            temp += value
            self.value = temp
        finally:
            logging.debug('released a lock')
            self.lock.release()

if __name__ == '__main__':
    A = bankAcc(10)

    B = bankAcc(3)

    for i in (range(3)):
        t = threading.Thread(target=deposit, args=(A,B))
        t.start()

    for i in range(3):
        t = threading.Thread(target=withdraw, args=(A,B))
        t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    print ('A: %d B %d', A.value,B.value)
