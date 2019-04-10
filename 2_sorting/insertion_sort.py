# Source GeeksForGeeks

# Function to sort our a_list in place
def insertion_sort(a_list): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(a_list)): 
  
        key = a_list[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < a_list[j] : 
                a_list[j+1] = a_list[j] 
                j -= 1
        a_list[j+1] = key 

    # now a_list is sorted! 

sample_input = [9,4,2,3,5,6,8,1,7]
insertion_sort(sample_input)
print(sample_input) # [1,2,3,4,5,6,7,8,9]