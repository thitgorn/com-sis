CHUNK = 1000 bytes
# def slave():
# {
    # lock.acquire()
    #  while  buffer is empty
        #   bufferEmpty.wait()
       
    # ... get item ...
    # bufferFull.notify()
    # lock.release()

#   .. process the counting....
    # lock2.acquire()
    # put the answer in the answer queue
#    lock2. release()
    
# }


# def master():   
    # create 4 consumer threads
#    ... start timer...
    # while (not eof data file) {
    #   lock.acquire()
    #   if buffer is not full
        #  data = read 1000 bytes.
         
        #  send data to the buffer.
         
        
        #  bufferEmpty.notify() // consumer queue
    #   else
        #  bufferFull.wait() 
    #   lock.release()
        
    # }
    # wait for all threads to finish
    # sum the answer in the answer queue.
  
    # ... end timer...
    # report the total count answer
    # report time used (seconds)...

if __name__ == '__main__':
    f = open("01all.nt")
    while True :
        data = f.read(CHUNK)
        print (data)
        if data=='' :
            break