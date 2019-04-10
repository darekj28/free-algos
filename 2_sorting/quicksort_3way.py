# Source GeeksForGeeks

# Python program to sort an array with 0,1 and 2 in a single pass 
  
# Function to sort array with 3 distinct elements
def quicksort_3way(a_list, arr_size): 
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi: 
        if a_list[mid] == 0: 
            a_list[lo],a_list[mid] = a_list[mid],a_list[lo] 
            lo = lo + 1
            mid = mid + 1
        elif a_list[mid] == 1: 
            mid = mid + 1
        else: 
            a_list[mid],a_list[hi] = a_list[hi],a_list[mid]  
            hi = hi - 1
    return a_list

sample_input = [2,1,2,1,0,0,1,2,0,1,2]
quicksort_3way(sample_input, len(sample_input))
print(sample_input) # [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]