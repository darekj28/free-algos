# 5.1 - String Sorts

__LSD radix sort.__ Program [lsd.py](lsd.py) implements LSD radix sort for fixed length strings. It includes a method for sorting 32-bit integers, treating each integer as a 4-byte string. When N is large, this algorithm is 2-3x faster than the system sort.

__MSD radix sort.__ Program [msd.py](msd.py) implements MSD radix sort.


Visualizations and descriptions of the above algorithms can be founds [here](http://www.cs.princeton.edu/courses/archive/spr13/cos226/lectures/51StringSorts.pdf)

# Review Exercises 
1. __Frequency counts.__ Read in a list of strings and print out their frequency counts. Algorithm: read strings into an array, 3-way radix quicksort them, and compute their frequency counts. Bonus speedup: compute the counts during the 3-way partitioning. Disadvantage: uses space to store all the strings. Alternate: TST.
2. __Sorting uniformly distributed data.__ Given N random real numbers from [0, 1], consider the following algorithm for sorting them: Partition [0, 1] into N equally spaced sub-intervals. Rearrange (ala cumulative counts) the N elements so that each element is in its appropriate bucket. Insertion sort the elements in each bucket (or equivalently, just insertion sort the whole file). That is, MSD radix sort for one level, then cutoff to insertion sort. [Try to do in-place?] Solution: It will take O(N) time in total on average. Let n_i be the number of elements in bucket i. The expected time to insertion sort all of the buckets is O(n) since `E[sum_i (n_i)^2] <= 2n`.
3. Given an array of N decimal integers of different lengths, describe how to sort them in O(N + K) time, where K is the total number of digits overall all the N integers.
4. __American flag sort.__ (in-place key-indexed counting) Given an array with N distinct values between 0 and R-1, rearrange them in ascending order in linear time and with O(R) extra space. Leads to an (essentially) in-place string sort. Hint:: compute the count[] array, which tells you where the keys need to go. Scan over the input array. Take the first key, find the bin in which it belong, and swap it into place (updating the corresponding count[] entry). Repeat with the second key, but be careful to skip over keys already known to be where they belong.