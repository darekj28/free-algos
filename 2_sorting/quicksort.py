# Source GeeksForGeeks

# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(a_list,low,high): 
	i = ( low-1 )         # index of smaller element 
	pivot = a_list[high]     # pivot 
  
	for j in range(low , high): 
  
		# If current element is smaller than or 
		# equal to pivot 
		if   a_list[j] <= pivot: 
		  
			# increment index of smaller element 
			i = i+1 
			a_list[i],a_list[j] = a_list[j],a_list[i] 
  
	a_list[i+1],a_list[high] = a_list[high],a_list[i+1] 
	return ( i+1 ) 
  
# The main function that implements QuickSort 
# a_list[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quicksort 
def quicksort(a_list,low,high): 
	if low < high: 
  
		# pi is partitioning index, a_list[p] is now 
		# at right place 
		pi = partition(a_list,low,high) 
  
		# Separately sort elements before 
		# partition and after partition 
		quicksort(a_list, low, pi-1) 
		quicksort(a_list, pi+1, high) 


sample_input = [9,4,2,3,5,6,8,1,7]
quicksort(sample_input, 0, len(sample_input)-1)
print(sample_input) # [1,2,3,4,5,6,7,8,9]