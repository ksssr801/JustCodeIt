# Implementing Linked List
# Insertion : Runs in O(1) time but for given key, T = O(n) in worst case.
# Deletion : Runs in O(1) time but for given key, T = O(n) in worst case.
# Searching : For 'n' size list, T = O(n) in worst case

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self, new_node, pos=None):
		self.size += 1
		count = 1
		curr_node = self.head
		if pos == None or pos > self.size:
			pos = self.size
		if self.head is None:
			self.head = new_node
		elif pos < 2:
			new_node.next = self.head
			self.head = new_node
		else:
			while count < (pos - 1):
				curr_node = curr_node.next
				count += 1
			if curr_node.next == None:
				curr_node.next = new_node
			else:
				temp_node = curr_node.next
				curr_node.next = new_node
				new_node.next = temp_node

	def delete(self, pos=None):
		count = 1
		curr_node = self.head
		if pos == None or pos > self.size:
			pos = self.size
		if self.head == None:
			self.size += 1
			print "LL is empty."
		elif pos < 2:
			self.head = self.head.next
		else:
			while count < (pos - 1):
				curr_node = curr_node.next
				count += 1
			temp_node = curr_node.next
			curr_node.next = temp_node.next
		self.size -= 1

	def search(self, value=None):
		count = 0
		pos_list = []
		curr_node = self.head
		if value == None:
			print 'Wrong value provided or value not present!'
		else:
			while curr_node is not None:
				count += 1
				if curr_node.data == value:
					pos_list.append(count)
				curr_node = curr_node.next
			if len(pos_list):
				print 'Given value found at position(s) : ', pos_list
			else:
				print 'Given value not found or LL is empty.'

	def print_LL(self):
		l_list = []
		curr_node = self.head
		while True:
			if curr_node is not None:
				l_list.append(curr_node.data)
				curr_node = curr_node.next
			else:
				break
		print 'Linked List : ', l_list
		print 'Length of LL : ', self.size

LL = LinkedList()

while True:
	print ('\nLinked List\n')
	print ('Select from options:')
	print ('1 : Insert')
	print ('2 : Delete')
	print ('3 : Search')
	print ('4 : Print')
	print ('0 : Exit')
	inp = input('Enter your choice : ')
	if inp == 0:
		break
	else:
		if inp == 1:
			data = input('Enter data: ')
			pos = input('Enter position: ')
			node = Node(data)
			LL.insert(node, pos)
		elif inp == 2:
			pos = input('Enter position: ')
			LL.delete(pos)
		elif inp == 3:
			val = input('Enter value: ')
			LL.search(val)
		elif inp == 4:
			LL.print_LL()
		else:
			print ("Wrong Choice!")
