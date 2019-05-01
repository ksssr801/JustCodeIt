# Implementing Queue, FIFO, T = O(1) for enqueue and dequeue


class Queue:
	def __init__(self):
		self.Q = []
		self.front = -1
		self.rear = -1
		self.count = 0

	def is_Q_empty(self):
		return self.Q == []

	def enqueue(self, data):
		if_empty = self.is_Q_empty()
		if if_empty:
			self.Q.append(data)
			self.front += 1
			self.rear += 1
		else:
			self.Q.append(data)
			self.rear += 1

	def dequeue(self):
		if_empty = self.is_Q_empty()
		if if_empty:
			print ("Q is empty.")
		else:
			del self.Q[self.front]

	def print_Q(self):
		if_empty = self.is_Q_empty()
		if if_empty:
			print ("Q is empty.")
		else:
			# python < 3.6
			print ("Current Q is {}".format(self.Q))
			print ("Current Q front is {}".format(self.count))
			print ("Current Q rear is {}".format(self.rear))
			# python > 3.5
			# print f"Current Q is {self.Q}{self.Q[0]}"
			# print f"Current Q front is {self.count}"
			# print f"Current Q rear is {self.rear}"
		self.count += 1


q = Queue()
# while True:
# 	print ('\nQueue\n')
# 	print ('Select from options:')
# 	print ('1 : Enqueue')
# 	print ('2 : Dequeue')
# 	print ('3 : Print')
# 	print ('0 : Exit')
# 	inp = input('Enter your choice : ')
# 	if inp == 0:
# 		break
# 	else:
# 		if inp == 1:
# 			data = input('Enter data: ')
# 			q.enqueue(data)
# 		elif inp == 2:
# 			q.dequeue()
# 		elif inp == 3:
# 			q.print_Q()
# 		else:
# 			print ("Wrong Choice!")
