# Implementing Stack, LIFO, T = O(1) for push and pop


class Stack:
	def __init__(self):
		self.stack = []
	
	def is_stack_empty(self):
		return self.stack == []

	def push_data(self, value):
		self.stack.append(value)
		print 'Updated Stack is', self.stack

	def pop_data(self):
		if_empty = self.is_stack_empty()
		if if_empty:
			print 'Stack is empty!'
		else:
			self.stack.pop()
			print ("Updated Stack is"), self.stack

	def print_stack(self):
		if_empty = self.is_stack_empty()
		if if_empty:
			print 'Stack is empty!'
		else:
			print 'Current Stack is ', self.stack


stk_obj = Stack()
while True:
	print ('\nStack\n')
	print ('Select from options:')
	print ('1 : Push')
	print ('2 : Pop')
	print ('3 : Print')
	print ('0 : Exit')
	inp = input('Enter your choice : ')
	if inp == 0:
		break
	else:
		if inp == 1:
			data = input('Enter data: ')
			stk_obj.push_data(data)
		elif inp == 2:
			stk_obj.pop_data()
		elif inp == 3:
			stk_obj.print_stack()
		else:
			print 'Wrong Choice!'
