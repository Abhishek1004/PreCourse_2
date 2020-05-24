# Python program for implementation of Quicksort

# This function is same in both iterative and recursive


#time complexity - O(nlogn) avg case, O(n^2) worst
#space complexity - O(logn) avg case and O(n) worst (additional space in stack)

def partition(arr, l, h):
#write your code here
	pivot = arr[h]
	i = l-1
	for j in range(l, h):
		if arr[j] < pivot:
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[i+1], arr[h] = arr[h], arr[i+1]
	return i+1

def quickSortIterative(arr, l, h):
#write your code here
	stack = [(l,h)]
	while stack:
		l, h = stack.pop()
		if l>=h:
			continue
		piv = partition(arr, l, h)
		stack.append((l, piv-1))
		stack.append((piv+1,h))

arr = [465, 412, 725, 23, 4645, 2910, 819]
quickSortIterative(arr, 0, len(arr)-1)
print(*arr)