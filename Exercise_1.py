# Python code to implement iterative Binary  
# Search. 

#time_complexity - O(logn)
#space_complexity - O(1)
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
	#write your code here
	if l<r:
		mid = l + ((r-l)//2)
		if arr[mid] == x:
			return mid
		elif x<arr[mid]:
			return binarySearch(arr, l, mid-1, x)
		else:
			return binarySearch(arr, mid+1, r, x)
	else:
		return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
	print ("Element is present at index % d" % result )
else: 
	print("Element is not present in array")
