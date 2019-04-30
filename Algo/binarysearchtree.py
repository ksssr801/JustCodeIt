# Implementing Binary Search Tree
# It takes T = O(n) time to walk an n-node BST
# Inserting & Searching a node in BST takes T = O(h) where h = height of the tree

import queue

class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None
		self.dups = 0

class BinarySearchTree:
	def __init__(self):
		self.height = -1
		self.Q_obj = queue.Queue()
		self.bfs_list = []
		self.preorder_list = []
		self.inorder_list = []
		self.postorder_list = []

	def insert(self, curr_root, new_node, level=1):
		if curr_root is None:
			curr_root = new_node
			curr_root.dups += 1
			print '\nNode %s is inserted at level %s.' % (curr_root.data, level)
			if level > self.height:
				self.height = level - 1
		elif new_node.data < curr_root.data:
			level += 1
			curr_root.left = self.insert(curr_root.left, new_node, level)
		elif new_node.data > curr_root.data:
			level += 1
			curr_root.right = self.insert(curr_root.right, new_node, level)
		else:
			curr_root.dups += 1
			print '\nDuplicate entry(%s times) for the node %s. Not inserted!' % (curr_root.dups, new_node.data)
		return curr_root

	def search(self, curr_root, data, level=1, flag='root node'):
		if curr_root is None:
			print '\nSearched node %s is not found or tree is empty!' % data
		elif data < curr_root.data:
			if level == 1:
				flag = 'left of root node'
			level += 1
			curr_root.left = self.search(curr_root.left, data, level, flag)
		elif data > curr_root.data:
			if level == 1:
				flag = 'right of root node'
			level += 1
			curr_root.right = self.search(curr_root.right, data, level, flag)
		else:
			print '\nSearched node %s found at level %s (%s)!' % (data, level, flag)
		return curr_root

	def min_node(self, curr_root):
		if curr_root is not None:
			while curr_root.left is not None:
				curr_root = curr_root.left
			return curr_root.data

	def max_node(self, curr_root):
		if curr_root is not None:
			while curr_root.right is not None:
				curr_root = curr_root.right
			return curr_root.data

	def find_height(self):
		return self.height

	# Breadth First Search
	def level_order_traverse(self, curr_root):
		if curr_root is not None:
			self.Q_obj.enqueue(curr_root)
			is_Q_empty = False
			while is_Q_empty is False:
				curr_root = self.Q_obj.Q[self.Q_obj.front]
				self.bfs_list.append(curr_root.data)
				if curr_root.left is not None:
					self.Q_obj.enqueue(curr_root.left)
				if curr_root.right is not None:
					self.Q_obj.enqueue(curr_root.right)
				self.Q_obj.dequeue()
				is_Q_empty = self.Q_obj.is_Q_empty()
			self.Q_obj.front = -1
		return self.bfs_list

	# Depth First Search
	def preorder(self, curr_root):
		if curr_root is not None:
			self.preorder_list.append(curr_root.data)
			self.preorder(curr_root.left)
			self.preorder(curr_root.right)
		return self.preorder_list
		self.preorder_list = []

	# Depth First Search
	def inorder(self, curr_root):
		if curr_root is not None:
			self.inorder(curr_root.left)
			self.inorder_list.append(curr_root.data)
			self.inorder(curr_root.right)
		return self.inorder_list
		self.inorder_list = []

	# Depth First Search
	def postorder(self, curr_root):
		if curr_root is not None:
			self.postorder(curr_root.left)
			self.postorder(curr_root.right)
			self.postorder_list.append(curr_root.data)
		return self.postorder_list
		self.postorder_list = []

root = None
bst = BinarySearchTree()
while True:
	print ('\nBinary Search Tree\n')
	print ('Select from options:')
	print ('1 : Insert')
	print ('2 : Search')
	print ('3 : Root Node, Min Node, Max Node & Tree Height')
	print ('4 : BFS Traversal')
	print ('5 : DFS Traversal')
	print ('0 : Exit')
	inp = input('Enter your choice : ')
	if inp == 0:
		break
	else:
		if inp == 1:
			data = raw_input('Enter data: ')
			node = Node(data)
			root = bst.insert(root, node)
		elif inp == 2:
			data = raw_input('Enter data: ')
			bst.search(root, data)
		elif inp == 3:
			min_n = bst.min_node(root)
			max_n = bst.max_node(root)
			tree_height = bst.find_height()
			if tree_height == -1:
				print '\nTree is empty!'
			else:
				print '\n'
				print 'Root Node : ', root.data
				print 'Min Node : ', min_n
				print 'Max Node : ', max_n
				print 'Height of the tree : ', tree_height
		elif inp == 4:
			lvl_order = bst.level_order_traverse(root)
			if lvl_order == []:
				print '\nTree is empty!'
			else:
				print '\n'
				print 'BFS - Level Order Traversal : ', lvl_order
				bst.bfs_list = []
		elif inp == 5:
			pre = bst.preorder(root)
			inorder = bst.inorder(root)
			post = bst.postorder(root)
			if pre == []:
				print '\nTree is empty!'
			else:
				print '\n'
				print 'DFS - Preorder Traversal : ', pre
				bst.preorder_list = []
				print 'DFS - Inorder Traversal : ', inorder
				bst.inorder_list = []
				print 'DFS - Postorder Traversal : ', post
				bst.postorder_list = []
		else:
			print ("Wrong Choice!")
