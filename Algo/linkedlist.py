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

	def insert_ll(self, new_node, pos=None):
		self.size += 1
		count = 1
		curr_node = self.head
		if pos is None or pos > self.size:
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
			if curr_node.next is None:
				curr_node.next = new_node
			else:
				temp_node = curr_node.next
				curr_node.next = new_node
				new_node.next = temp_node

	def delete_ll(self, value=None):
		count = 1
		pos = 0
		curr_node = self.head
		if self.head is None:
			print ('LL is empty!')
		else:
			while curr_node.data is not value:
				pos += 1
				curr_node = curr_node.next
				if curr_node is None:
					break
			pos += 1
			if pos > self.size:
				print ('Provided value {} is not present in LL!'.format(value))  # python < 3.6
				# print f'Provided value {value} is not present in LL!'  # python > 3.5
			else:
				curr_node = self.head
				if pos < 2:
					self.head = self.head.next
				else:
					while count < (pos - 1):
						curr_node = curr_node.next
						count += 1
					temp_node = curr_node.next
					curr_node.next = temp_node.next
				self.size -= 1

	def search_ll(self, value=None):
		count = 0
		pos_list = []
		curr_node = self.head
		if value is None:
			print ('No value provided!')
		else:
			while curr_node is not None:
				count += 1
				if curr_node.data == value:
					pos_list.append(count)
				curr_node = curr_node.next
			if len(pos_list):
				print ('Given value {} found at position(s) : {}'.format(value, pos_list))  # python < 3.6
				# print f'Given value {value} found at position(s) : {pos_list}'  # python > 3.5
			else:
				print ('Given value not found or LL is empty.')

	def print_ll(self):
		l_list = []
		curr_node = self.head
		while True:
			if curr_node is not None:
				l_list.append(curr_node.data)
				curr_node = curr_node.next
			else:
				break
		# python < 3.6
		print ('Linked List : {}'.format(l_list))
		print ('Length of LL : {}'.format(self.size))
		# python > 3.5
		# print f'Linked List : {l_list}'
		# print f'Length of LL : {self.size}'


LL = LinkedList()

# while True:
# 	print ('\nLinked List\n')
# 	print ('Select from options:')
# 	print ('1 : Insert')
# 	print ('2 : Delete')
# 	print ('3 : Search')
# 	print ('4 : Print')
# 	print ('0 : Exit')
# 	inp = input('Enter your choice : ')
# 	if inp == 0:
# 		break
# 	else:
# 		if inp == 1:
# 			data = input('Enter data: ')
# 			pos = input('Enter position: ')
# 			node = Node(data)
# 			LL.insert_ll(node, pos)
# 		elif inp == 2:
# 			val = input('Enter value: ')
# 			LL.delete_ll(val)
# 		elif inp == 3:
# 			val = input('Enter value: ')
# 			LL.search_ll(val)
# 		elif inp == 4:
# 			LL.print_ll()
# 		else:
# 			print ("Wrong Choice!")
