#time_complexity - O(n)
#space_complexity - O(n)


# Node class  
class Node:  
  
	# Function to initialise the node object  
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList: 
  
	def __init__(self):
		self.head = None
		
  
	def push(self, new_data):
		new = Node(new_data)
		new.next = self.head
		self.head = new

		
  
	# Function to get the middle of  
	# the linked list 
	def printMiddle(self):
		slow, fast = self.head, self.head
		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next
		print(slow.data)

# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
