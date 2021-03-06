 #!/usr/local/bin/python
class NodeT:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value

class SpecialTNode:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value
		self.nextRight = None

class Tree:
	def __init__(self):
		self.root = None

# functions for tree traversal
# in-order traversal - the natural order, left to right via root
def inOrderTraversal(root):
	if root != None:
		inOrderTraversal(root.left)
		print(root.value)
		inOrderTraversal(root.right)

# in-order traversal - returning list
def _inorderTraversal(root, l):
	if root == None:
		return 
        
	_inorderTraversal(root.left, l)
	l.append(root)
	_inorderTraversal(root.right, l)
    
def inorderTraversal(root):
	soln = []
	_inorderTraversal(root,soln)
	return soln

# pre-order traversal - the order where root is given pre-dominance
def preOrderTraversal(root):
	if root != None:
		print(root.value)
		preOrderTraversal(root.left)
		preOrderTraversal(root.right)

def preOrderTraversalNonRec(root):
	if root == None:
		return 
	curr = root
	stack = []
	
	
	while curr != None  or len(stack) != 0:	
		while curr != None:
			stack.append(curr)
			curr = curr.left

	'''
		the while loop will be exited when there are no more left children
		in that case pop the stack, print it and then look in its right child
	'''
	
		if curr == None and len(stack) != 0:
			curr = stack.pop()
			print(curr.value)
			curr = curr.right 
		
# constructing tree from pre and in order

def construct_tree(in_order_arr, pre_order_arr, in_start, in_end):
	if in_start > in_end:
		return 

	tNode = NodeT(pre_order_arr[global_pre_index])
	global_pre_index += 1

	if in_start == in_end:
		return tNode

	root_index_in_order = in_order_arr.index(tNode.val)
	left_index = construct_tree(in_order_arr, pre_order_arr, in_start, root_index_in_order-1)
	right_index = construct_tree(in_order_arr, pre_order_arr, root_index_in_order+1, in_end)

	return tNode

# pre-order traversal - the order where root is given last priority, children first
def postOrderTraversal(root):
	if root != None:
		preOrderTraversal(root.left)
		preOrderTraversal(root.right)	
		print(root.value)

def RecDFS(root): # Same as the logic for pre-order. Thus can be done using Stack too.
	if root == None:
		return
	else:
		print(root.value)
		RecDFS(root.left)
		RecDFS(root.right)

# DFS using stacks
def NonRecDFS(root):
	if root == None:
		return 
	else:
		stck = []
		stck.append(root)
		while len(stck) != 0:
			curr = stck.pop()
			if curr.right != None:
				stck.append(curr.right)

			if curr.left != None:
				stck.append(curr.left)
			
			print(curr.value)
		return

def BFSUsingQ(root):
	queue = []
	curr = root
	i = 0
	## append the root node
	queue.append(curr)

	while curr != None:
		queue.append(curr.left)
		queue.append(curr.right)
		i += 1
		curr = queue[i]

	for i in queue:
		if i != None:
			print(i.value)

def heightFrom(node):
	if node == None: # Base case, you are the leaf node
		return 0
	else:
		return 1 + max(heightFrom(node.left),heightFrom(node.right))

def diameter(root):
	# root case: empty tree - 0 diameter
	if root == None:
		return 0
	else:
		''' 
		Case 1: 
			diameter forming node path passes through the root node.
			In that case the diameter = height(left sub tree) + height (right sub tree)
		'''
		lHeight = heightFrom(root.left)
		rHeight = heightFrom(root.right)

		'''
		Case 2: 
			Diameter forming nodes might not necessarily pass through the root nodes.
			In that case, for every left and right node, the diameter has to be calculated
		'''
		lDiameter = diameter(root.left)
		rDiameter = diameter(root.right)

		# Finally, the diameter would be either lDiameter, rDiameter or lHeight + rHeight + 1
		return max(lHeight+rHeight+1, lDiameter, rDiameter)


# stack methods - note, these method are built in for lists
def push(arr,num):
	arr.append(num)

def pop(arr):
	l = len(arr)
	ele = arr[l-1]
	arr = arr[:l-1]
	return arr,ele

def inOrderTraversalUsingStack(root):
	#run1 = True # needed for entering the loop once
	curr = root
	stack = []

	while curr != None:
		while curr != None:
			push(stack,curr)
			curr = curr.left

		while curr == None and len(stack) > 0:
			stack,curr = pop(stack)
			print(curr.value)
			curr = curr.right	

def lvl_ordr_trav_new_line(root):
	curr_lvl = [root]
	nxt_lvl = []

	while len(curr_lvl) != 0:
		for node in curr_lvl:
			if node.left: 
				nxt_lvl.append(node.left)
			if node.right:
				nxt_lvl.append(node.right)
			print(node.value, end=" ")
		print()
		curr_lvl = nxt_lvl
		nxt_lvl = []

def lvl_ordr_trav_same_line(root):
	if root == None:
		return
	res = []
	q = [root]
	while len(q) > 0:
		ele = q.pop(0)
		print(ele.value)
		res.append(ele)
		if ele.left:
			q.append(ele.left)
		if ele.right:
			q.append(ele.right)
	return res

# a much better solution is possible using two queues
def printLevelK(root, k):
	if root == None:
		return 
	else:
		q = [root]
		level = 1
		while level != k and len(q) != 0:
			level += 1
			currLvlNodes = []

			while len(q) != 0:
				currLvlNodes.append(q.pop())

			for node in currLvlNodes:
				if node.left != None:
					q.append(node.left)
				if node.right != None:
					q.append(node.right)

		for node in q:
			print(node.value)

		return

def nodesAtDistK(root, k):
	if not root:
		return

	if k == 0: # destination reached
		print(root.value)

	# k > 0
	nodesAtDistK(root.left, k-1)
	nodesAtDistK(root.right, k-1)

# this function will return a tree given pre-order and in-order traversal
def ConstructTreeInPre(inOrder,preOrder,inStart,inEnd):
	
	if inStart > inEnd:
		return None

	item = preOrder[ConstructTreeInPre.preIndex]
	node = NodeT(item)
	ConstructTreeInPre.preIndex += 1 #global variable

	if inStart == inEnd: # leaf node reached. No more children to this node
		return node

	rightChildIndex = inOrder.index(item) + 1
	leftChildIndex = inOrder.index(item) - 1

	# left sub-tree is the part of the in-order array from start to index of node ele - 1 
	node.left = ConstructTreeInPre(inOrder,preOrder,inStart,leftChildIndex) 
	# right sub-tree is the part of the in-order array from index of node ele + 1 to end
	node.right = ConstructTreeInPre(inOrder,preOrder,rightChildIndex,inEnd)

	return node

# this function will return a tree given pre-order and in-order traversal - method faulty
def ConstructTreeInPost(inOrder,postOrder,inStart,inEnd):
	if inStart > inEnd:
		return None

	item = postOrder[ConstructTreeInPost.postIndex]
	ConstructTreeInPost.postIndex -= 1
	node = NodeT(item)
	

	if inStart == inEnd or ConstructTreeInPost.postIndex <= 0:
		return node


	leftChildIndex = inOrder.index(item) - 1
	rightChildIndex = inOrder.index(item) + 1
	node.left = ConstructTreeInPost(inOrder,postOrder,inStart,leftChildIndex)
	node.right = ConstructTreeInPost(inOrder,postOrder,rightChildIndex,inEnd)

	return node

def getWidth(root,i):
	if root is None:
		return 0
	if i == 1: # root level
		return 1
	else:
	# width of left subtree + width of right subtree
		return getWidth(root.left,i-1)+getWidth(root.right,i-1)


def getMaxWidth(root):
	max = 0
	for i in range(1,heightFrom(root)+1):
		width = getWidth(root,i)
		if max < width:
			max = width

	print("Maximum width of the tree is: %d" %max)

def printKawayFromRoot(root,k):
	if root == None: # to stop running into nodes beyond leaf
		return
	if k == 0: # base case
		print(root.value)
		return
	else:
		printKawayFromRoot(root.left,k-1)
		printKawayFromRoot(root.right,k-1)

def printAncestors(root,ele):
	if root == None:
		return False

	if root.value == ele:
		return True
	else:
		if printAncestors(root.left,ele) == True or printAncestors(root.right,ele) == True:
			print(root.value)
			return True


def connectNodesSameLvl(root):
	if not root:
		return 

	curr_lvl = [root]
	nxt_lvl = []

	while len(curr_lvl) != 0:
		# loop 1: For enqueing the next level children to nxt_lvl
		for node in curr_lvl:
			if node.left:
				nxt_lvl.append(node.left)
			if node.right:
				nxt_lvl.append(node.right)

		# loop 2: Actual connections
		for i in range(1,len(curr_lvl)):
			curr_lvl[i-1].nextRight = curr_lvl[i]

		# make nxt_lvl curr_lvl
		curr_lvl = nxt_lvl 
		nxt_lvl = []
		
def _btree_to_bst(root, in_order_arr):
	if not root:
		return

	_btree_to_bst(root.left, in_order_arr)
	root = in_order_arr.pop(0)
	_btree_to_bst(root.right, in_order_arr)	

def btree_to_bst(root):
	in_order_arr = inorderTraversal(root)
	in_order_arr = sorted(in_order_arr, key = lambda x : x.value)

	_btree_to_bst(root, in_order_arr)


def sum_tree(root):
	if not root:
		return 0
	else:
		return root.value + sum_tree(root.left) + sum_tree(root.right)

def tree_trimmer(root, h):
	if root == None:
		return root

	if h == 0:
		root.value = sum_tree(root)
		root.left = root.right = None

	tree_trimmer(root.left, h-1)
	tree_trimmer(root.right, h-1)
	

def is_balanced(root): # worst case complexity - when the tree is actually balanced will be O(n^2)
	if root == None:
		return True

	if abs(heightFrom(root.left) - heightFrom(root.right)) <= 1:
		return is_balanced(root.left) and is_balanced(root.right)
	else:
		return False

def _optimized_height(root):
	if root == None:
		return 0

	l_height = _optimized_height(root.left) 
	if l_height == -1: # in case, you find a mis-match, you say its an error and the method should return -1
		return -1

	r_height = _optimized_height(root.right)
	if r_height == -1:
		return -1

	if abs(l_height-r_height) <= 1: # balanced till this point
		return 1 + max(l_height, r_height)
	else:
		return -1 # this is the error code we want to propogate all the way to the top, once we get it. 

def is_balanced_optimized(root):
	return _optimized_height(root) != -1


'''
	The trick in the sort of the problems which is about paths in trees
	The helper method always updates a static variable
	The helper method returns the maximum/minimum child of the current node. This is how we keep track of the partial solution.
'''

def _max_sum_tree_path(root, max_sum):
	if root == None:
		return 0

	l_sum = _max_sum_tree_path(root.left, max_sum)
	r_sum = _max_sum_tree_path(root.right, max_sum)

	'''
		There are total 4 cases which could contribute to it being the highest sum path
		* root itself
		* root + left sub-child
		* root + right sub-child
		* root + left + right sub-children
	'''
	max_sum[0] = max(root.value, root.value + l_sum, root.value + r_sum, root.value + l_sum + r_sum, max_sum[0])

	return root.value + max(l_sum, r_sum)

def max_sum_tree_path(root):	
	max_sum = [-float('inf')]
	_max_sum_tree_path(root, max_sum)
	return max_sum[0]


def _leaf_to_leaf_max_sum(root, max_sum):
	if root == None:
		return 0

	l_sum = _leaf_to_leaf_max_sum(root.left, max_sum)
	r_sum = _leaf_to_leaf_max_sum(root.right, max_sum)

	if root.left and root.right: # the question clearly says leaf-to-leaf. Change the value only when there is indeed a left and right child
		max_sum[0] = max(root.value + l_sum + r_sum, max_sum[0])

	return max(l_sum, r_sum) + root.value

def leaf_to_leaf_max_sum(root):
	max_sum = [-float("inf")]

	_leaf_to_leaf_max_sum(root, max_sum)

	return max_sum[0]

def _number_of_paths(root, sum, count_path):
	if root == None:
		return 0

	l_sum = _number_of_paths(root.left, sum, count_path)
	r_sum = _number_of_paths(root.right, sum, count_path)

	if sum == root.value:
		count_path[0] += 1

	if sum == root.value + l_sum:
		count_path[0] += 1

	if sum == root.value + r_sum:
		count_path[0] += 1

	if sum == root.value + l_sum+ r_sum:
		count_path[0] += 1

	return max(l_sum, r_sum) + root.value

# last problem cracking the coding interview
def number_of_paths(root, sum):
	count_path = [0]

	_number_of_paths(root, sum, count_path)

	return count_path[0]


## TEST DRIVER ####################

t1 = Tree()

t1.root = NodeT(1)
t1.root.left = NodeT(2)
t1.root.right = NodeT(3)
t1.root.left.left = NodeT(4)
t1.root.left.right = NodeT(5)
t1.root.right.left = NodeT(6)
t1.root.right.right = NodeT(7)
t1.root.left.left.left = NodeT(8)
t1.root.right.left.left = NodeT(9)
t1.root.right.left.right = NodeT(10)


print("In order traversal")
inOrderTraversal(t1.root)
print("In order traversal using stack")
inOrderTraversalUsingStack(t1.root)
print("Pre order traversal")
preOrderTraversal(t1.root)
print("Post order traversal")
postOrderTraversal(t1.root)
print("Depth first search")
RecDFS(t1.root)
print("Breadth first search using queue")
BFSUsingQ(t1.root)
print("Height from root")
print(heightFrom(t1.root))

getMaxWidth(t1.root)

print("Nodes k away from the root, where k = 1")
printKawayFromRoot(t1.root,1)

print("Nodes k away from the root, where k = 2")
printKawayFromRoot(t1.root,2)

ConstructTreeInPre.preIndex = 0
inOrder = list('DBEAC')
preOrder = list('ABDEC')
newTree = Tree()
newTree.root = ConstructTreeInPre(inOrder,preOrder,0,len(inOrder)-1)
print("In order traversal of newly constructed tree. Expected DBEAC")
inOrderTraversal(newTree.root)

## Faulty method

postOrder = list('DEBCA')
ConstructTreeInPost.postIndex = len(postOrder) - 1
newTree = Tree()
newTree.root = ConstructTreeInPost(inOrder,postOrder,0,len(inOrder)-1)
print("In order traversal of newly constructed tree. Expected DBEAC")
inOrderTraversal(newTree.root)

print("Print ancestors of elements")
printAncestors(t1.root,5)

t4 = Tree()

t4.root = NodeT(10)
t4.root.left = NodeT(5)
t4.root.left.left = NodeT(3)
t4.root.left.left.left = NodeT(3)
t4.root.left.left.right = NodeT(-2)
t4.root.left.right = NodeT(2)
t4.root.left.right.right = NodeT(1)
t4.root.right = NodeT(-3)
t4.root.right.right = NodeT(11)