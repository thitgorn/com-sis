import sys
import random
import time
import threading

value = 1
value_lock = threading.Lock()
count = 0

class Producer(threading.Thread):
	def __init__(self, items, can_produce, can_consume):
		threading.Thread.__init__(self)
		self.items = items
		self.can_produce = can_produce
		self.can_consume = can_consume


	def produce_item(self):
		global value
		value_lock.acquire()
		value = value + 1
		value_lock.release()
		self.items.append(value)
		print ("{}: i produced an item {}".format(self.name,value))

	def wait(self):
		time.sleep(random.uniform(0, 3))
		# time.sleep(2)

	def run(self):
		global count
		while 1:
			self.wait()
			count += 1
			self.can_produce.acquire()
			count -= 1
			self.produce_item()
			self.can_consume.release()

class Consumer(threading.Thread):
	def __init__(self, items, can_produce, can_consume):
		threading.Thread.__init__(self)
		self.items = items
		self.can_produce = can_produce
		self.can_consume = can_consume

	def consume_item(self):
		item = self.items.pop()
		print ("{}: i consumed an item {}".format(self.name,item))

	def wait(self):
		time.sleep(random.uniform(0, 3))
		# time.sleep(2)

	def run(self):
		global count
		while 1:
			self.wait()
			count += 1
			self.can_consume.acquire()
			count -= 1
			self.consume_item()
			self.can_produce.release()

def usage(script):
	print ("Usage:\t%s count_producers count_consumers buffer_length" % script)

class Counter(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global count
		while 1:
			print ("Waitting thread %d" % count)
			time.sleep(1)

if __name__ == "__main__":

	if len(sys.argv) != 4:
		usage(sys.argv[0])
		sys.exit(0)
	value = 1
	count_producers = int(sys.argv[1])
	count_consumers = int(sys.argv[2])
	buffer_length = int(sys.argv[3])

	items = []
	producers = []
	consumers = []

	#acquire while buffer is not full
	can_produce = threading.Semaphore(buffer_length)

	#acquire while buffer is not empty
	can_consume = threading.Semaphore(0)

	for i in range(count_producers):
		producers.append(Producer(items, can_produce, can_consume))
		# thread . start
		producers[-1].start()

	for i in range(count_consumers):
		consumers.append(Consumer(items, can_produce, can_consume))
		consumers[-1].start()

	counter = Counter()
	counter.start()
	for p in producers:
		p.join()

	for c in consumers:
		c.join()
