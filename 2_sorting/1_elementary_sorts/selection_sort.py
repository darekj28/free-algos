# Source GeeksForGeeks

# this method sorts the input unsorted_list in place
def selection_sort(a_list):
	# Traverse through all array elements
	for i in range(0, len(a_list)):
		 
		# Find the minimum element in remaining 
		# unsorted array
		min_index = i
		for j in range(i + 1, len(a_list)):
			if a_list[min_index] > a_list[j]:
				min_index = j
				 
		# Swap the found minimum element with 
		# the first element        
		a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

	# now a_list is sorted!

sample_input = [9,4,2,3,5,6,8,1,7]
selection_sort(sample_input)
print(sample_input) # [1,2,3,4,5,6,7,8,9]