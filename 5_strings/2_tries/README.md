# 5.2 Tries

__Symbol tables with string keys.__ Could use standard symbol table implementation. Instead, exploit additional structure of string keys. Customized searching algorithms for strings (and other keys represented as digits). Goal: as fast as hashing, more flexible than binary search trees. Can efficiently support additional operations including prefix and wildcard matching, e.g., IP routing table wants to forward to 128.112.136.12, instead forwards to 128.112 which is longest matching prefix that it knows about. Side benefit: fast and space-efficient string searching.

__R-way tries.__ Program [trie_st.py](trie_st.py) implements a string symbol table using a multiway trie.

__Ternary search tries.__ Program [tst.py](tst.py) implements a string symbol table using a ternary search trie.

The slides [here](http://www.cs.princeton.edu/courses/archive/spr13/cos226/lectures/52Tries.pdf) provide an excellent visual representation of tries.

_Property A._ (Bentley-Sedgewick) Given an input set, the number of nodes in its TST is the same, regardless of the order in which the strings are inserted.

Proof. There is a unique node in the TST for each distinct string prefix in the set. The relative positions of the nodes within the TST can change depending on the insertion order, but the number of nodes is invariant.

__Advanced operations.__ Wildcard search, prefix match. The r-way trie and TST implementations include code for wildcard matching and prefix matching.

Lazy delete = change the word boundary bit. Eager delete = clean up any dead parent links.

Application: T9 text input for cell phones. User types using phone pad keys; system displays all words that correspond (and auto-completes as soon as it is unique). If user types 0, system displays all possible auto-completions.

# Review Exercises
1. Write nonrecursive versions of an R-way trie string set and a TST.
2. __Unique substrings of length L.__ Write a program that reads in text from standard input and calculate the number of unique substrings of length L that it contains. For example, if the input is `cgcgggcgcg` then there are 5 unique substrings of length 3: `cgc`, `cgg`, `gcg`, `ggc`, and `ggg`. Applications to data compression. Hint: use the string slicing `s[i:i+L]` to extract ith substring and insert into a hash table. 
3. __Unique substrings.__ Write a program that reads in text from standard input and calculates the number of distinct substrings of any length. (Can do very efficiently with a suffix tree.)
4. __Document similarity.__ To determine the similarity of two documents, calculate the number of occurrences of each trigram (3 consecutive letters). Two documents are similar if the Euclidean distance between the frequency vector of trigrams is small.
