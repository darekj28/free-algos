

# 2.1 Elementary Sorts
In this section, we shall study two elementary sorting methods (selection sort and insertion sort)

**Rules of the game.** Our primary concern is algorithms for rearranging arrays of items where each item contains a key. The objective is to rearrange the items such that their keys are in ascending order. With but a few exceptions, our sort code refers to the data only through two operations: the method _less()__ that compares objects and the method _exch()_ that exchanges them.

```
# returns a boolean that evaluates (v < m) 
# using the compareTo method
def less(v, w):
   return (v.compareTo(w) < 0)

# swaps the i,j indices in the input list
def exch(a_list, index_i, index_j):
   a_list[i], a_list[j] = a_list[j], a_list[i]
```

- *Sorting cost model*. When studying sorting algorithms, we count compares and exchanges. For algorithms that do not use exchanges, we count array accesses.

- *Extra memory*. The sorting algorithms we consider divide into two basic types: those that sort in place (no extra memory except perhaps for a small function-call stack or a constant number of instance variables), and those that need enough extra memory to hold another copy of the array to be sorted.
Types of data. Our sort code is effective for any type of data that is a **Comparable**. This means that there is a method *compareTo()* for which _v.compareTo(w)_ returns an integer that is negative, zero, or positive when _v < w, v = w, or v > w_, respectively. The *compareTo()* method must be a total ordering meaning the following 3 properties are satisfied:
    - *Reflexive:* for all _v, v = v_.
    - *Antisymmetric:* for all _v_ and _w_, if (_v_ < _w_) then (_w_ > _v_); and if (_v = w_) then (_w = v_).
    - *Transitive:* for all _v, w_, and _x_, if (_v ≤ w_) and (_w ≤ x_), then _v ≤ x_.
In addition, *v.compareTo(w)* must throw an error if _v_ and _w_ are of incompatible types or if either is null.

Below is an example of a *compareTo* 


**Selection sort.** One of the simplest sorting algorithms works as follows: First, find the smallest item in the array, and exchange it with the first entry. Then, find the next smallest item and exchange it with the second entry. Continue in this way until the entire array is sorted. This method is called selection sort because it works by repeatedly selecting the smallest remaining item. [selection_sort.py](selection_sort.py) is an implementation of this method.

![selection_sort.png](selection.png)

**Proposition.** Selection sort uses _~N<sup>2</sup>/2_ compares and n exchanges to sort an array of length _N_.


**Insertion sort.** The algorithm that people often use to sort bridge hands is to consider the cards one at a time, inserting each into its proper place among those already considered (keeping them sorted). In a computer implementation, we need to make space for the current item by moving larger items one position to the right, before inserting the current item into the vacated position. [insertion_sort.py](insertion_sort.py) is an implementation of this method, which is called insertion sort.

![insertion_sort](insertion.png)

**Proposition.** For randomly ordered arrays of length _N_ with with distinct keys, insertion sort uses _~N<sup>2</sup>/4_ compares and _~N<sup>2</sup>/4_ exchanges on the average. The worst case is _~ N<sup>2</sup>/2_ compares and _~ N<sup>2</sup>/2_ exchanges and the best case is _N-1_ compares and _0_ exchanges.
Insertion sort works well for certain types of nonrandom arrays that often arise in practice, even if they are huge. An inversion is a pair of keys that are out of order in the array. For instance, E X A M P L E has 11 inversions: E-A, X-A, X-M, X-P, X-L, X-E, M-L, M-E, P-L, P-E, and L-E. If the number of inversions in an array is less than a constant multiple of the array size, we say that the array is partially sorted.

**Proposition.** The number of exchanges used by insertion sort is equal to the number of inversions in the array, and the number of compares is at least equal to the number of inversions and at most equal to the number of inversions plus the array size.

**Property.** For randomly ordered arrays of distinct values, the running times of insertion sort and selection sort are quadratic and within a small constant factor of one another.

**Visualizing sorting algorithms.** We use a simple visual representation to help describe the properties of sorting algorithms. We use vertical bars, to be sorted by their heights.


![sorting_bars](bars.png)

# Review Exercises

1. Show in the style of the example trace with selection sort, how selection sort sorts the array

```
E A S Y Q U E S T I O N
```

2. What is the maximum number of exchanges involving any particular item during selection sort? What is the average number of exchanges involving an item?

3. Show in the style of the example trace with insertion sort, how insertion sort sorts the array
```
E A S Y Q U E S T I O N
```

4. Which method runs fastest for an array with all keys identical, selection sort or insertion sort?

5. Suppose that we use insertion sort on a randomly ordered array where items have only one of three key values. Is the running time linear, quadratic, or something in between?

6. __Expensive exchange.__ A clerk at a shipping company is charged with the task of rearranging a number of large crates in order of the time they are to be shipped out. Thus, the cost of compares is very low (just look at the labels) relative to the cost of exchanges (move the crates). The warehouse is nearly full: there is extra space sufficient to hold any one of the crates, but not two. Which sorting method should the clerk use?

7. __Stupidsort.__ Analyze the running time (worst case and best case), correctness, and stability of the following sorting algorithm. Scan the array from left to right until you find two consecutive items that are out-of-place. Swap them, and start over from the beginning. Repeat until the scan reaches the end of the array.

```
for i in range(1, N):
    if (less(a[i], a[i-1])):
        exch(i, i-1)
        i = 0
```
Consider also the following recursive variant and analyze the worst case memory usage.
```
@staticmethod
def sort(a):
    for i in range(1, len(a)):
        if (less(a[i], a[i-1])):
            exch(i, i-1);
            sort(a);
```

8. __Bogosort.__ Bogosort is a randomized algorithm that works by throwing the N cards up in the air, collecting them, and checking whether they wound up in increasing order. If they didn't, repeat until they do. Implement bogosort using the shuffling algorithm from Section 1.4. Estimate the running time as a function of N.
