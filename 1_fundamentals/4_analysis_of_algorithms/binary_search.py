
# Source, Geeks for Geeks

class BinarySearch:
    # binary search 
    @staticmethod
    def binary_search(arr, x):
        return BinarySearch._binary_search(arr, 0, len(arr) - 1, x)

    #  Recursive helper function. Returns index of x in arr if present, else -1 
    @staticmethod
    def _binary_search (arr, l, r, x): 
      
        # Check base case 
        if r >= l: 
      
            mid = l + (r - l)/2
      
            # If element is present at the middle itself 
            if arr[mid] == x: 
                return mid 
              
            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            elif arr[mid] > x: 
                return BinarySearch._binary_search(arr, l, mid-1, x) 
      
            # Else the element can only be present  
            # in right subarray 
            else: 
                return BinarySearch._binary_search(arr, mid+1, r, x) 
      
        else: 
            # Element is not present in the array 
            return -1

