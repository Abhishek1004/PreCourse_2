# Python program for implementation of MergeSort 
#time_complexity - O(nlogn) - recursive divide and merge
#space_complexity - O(n) - storing left and right halves

def mergeSort(arr):
  
  #write your code here
	if len(arr)>1:
		mid = len(arr)//2
		lefthalf = arr[:mid]
		righthalf = arr[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				arr[k]=lefthalf[i]
				i=i+1
			else:
				arr[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			arr[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			arr[k]=righthalf[j]
			j=j+1
			k=k+1
  
# Code to print the list 
def printList(arr): 
	#write your code here
	print(*arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7]  
	print ("Given array is", end="\n")  
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 
