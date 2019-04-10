# 5.3 - Substring Search


High-performance pattern matching in Java for general string searching, searching with wildcards, and searching with character classes.

Program [brute.py](brute.py) is brute force string search. 

__Rabin-Karp.__ Program [rabin_karp.py](rabin_karp.py) implements the Rabin-Karp randomized fingerprint algorithm.

__Knuth-Morris-Pratt.__ Program [kmp.py](kmp.py) is Knuth-Morris-Pratt algorithm. 
__Boyer-Moore.__ Program [boyer_moore.py](booyer_moore.py) implements the bad-character rule part of the Boyer-Moore algorithm. It does not implement the strong good suffix rule.

Visualizations and descriptions of the above algorithms can be seen in the slides [here](http://www.cs.princeton.edu/courses/archive/spr13/cos226/lectures/53SubstringSearch.pdf).

# Review Exercises
1. Design a brute-force substring search algorithm that scans the pattern from right to left.
2. Determine the KMP DFA for the following pattern strings.
    - AAAAAAAB
    - AACAAAB
    - ABABABAB
    - ABAABAAABAAAB
    - ABAABCABAABCB
3. How would you modify Rabin-Karp to search for a given pattern with the additional proviso that the middle character is a "wildcard" (any text character at all can match it).
4. __Online palindrome detection.__ Read in characters one at a time. Report at each instant if the current string is a palindrome. Hint: use Karp-Rabin hashing idea.
5. __Suffix-prefix match.__ Design a linear-time algorithm to find the longest suffix of one string a that exactly matches a prefix of another string b.
6. __Cyclic rotation.__ Design a linear-time algorithm to determine whether one string is a cyclic rotation of another. A string a is a cyclic rotation of a string b if a and b have the same length and a consists of a suffix of b followed by a prefix of b.
7. __Substring of a circular string.__ Design a linear-time algorithm to determine whether one string a is a substring of a cirular string b.
8. __Longest palindromic substring.__ Given a string s, find the longest substring that is a palindrome (or a Watson-crick palindrome).
9. __Repeated substring.__ Given an integer K and a string of length N, find the longest substring which appears at least K times.
10. __Longest common substring.__ Given two (or three strings), find the longest substring that appears in all three. Hint: assume you know the length L of the longest common substring. Hash each substring of length L and check if any hash bucket contains (at least) one entry from each string.
11. __All matches.__ Modify KMP to find all matches in linear time (instead of leftmost match).
12. __Anagram substring search.__ Given a text string `txt[]` of length N and a pattern string `pat[]` of length M, determine whether `pat[]` or any of its anagrams (any of its M! permutations) appears in the text. Hint: maintain a histogram of the letter frequencies for a given substring of length M in the text.