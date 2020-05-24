# Python program for implementation of Quicksort Sort 
  

#time_complexity - O(nlogn) avg case, O(n^2) worst
#space_complexity - O(1)
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
	#write your code here
	pivot = arr[low]
	while True:
		while arr[low] < pivot:
			low += 1
		while arr[high] > pivot:
			high -= 1
		if low >= high:
			return high
		arr[low], arr[high] = arr[high], arr[low]
		low += 1
		high -= 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
	
	#write your code here
	if low < high:
		pivot = partition(arr, low, high)
		quickSort(arr, low, pivot)
		quickSort(arr, pivot+1, high)
	return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 
  
 
