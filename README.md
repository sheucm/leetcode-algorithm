# leetcode
The leetcode solutions for algorithm category writen in either C++ or Python.
(Only Median and Hard)

### Folder naming convention
```
<No>_<Topic>__<Title>
```

### C++ Version
Use c++11 or higher.
```
g++ -std=c++11  test.cpp
```

### Python Version
python3






# Grind 75 Questions
https://www.techinterviewhandbook.org/grind75








# Blind 75 Questions
https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions

### Blind75 LeetCode Note:

###### Array
```
Concept: Use some variables to iterate list
Problem Types:
1. Use "hash" table to iterate list. Example: 1. Two Sum: use hash (easy-O(N)-O(N))
2. Use "max" and "min" two variables to iterate list. Example: 121. Best Time to Buy and Sell Stock (easy-O(N)-O(1))
3. Use "prev" and "post" to iterate list. Example: 238. Product of Array Except Self (Medium-O(N)-O(1))
4. Use (max, min, or both) "DP" to iterate list. Example: 53. Maximum Subarray (Medium-O(N)-O(N)) / 152. Maximum Product Subarray (Medium-O(N)-O(N))
5. Use "left-right-medium" for "Binary Search" to loop the list. Example: 153. Find Minimum in Rotated Sorted Array (Medium-O(logN)-O(1)) / 33. Search in Rotated Sorted Array (Medium-O(logN)-O(1))
6. Use "Sort" and "left++ / right--" to iterate list. 15. 3Sum:  (Medium-O(N^2)-O(N)) / 11. Container With Most Water (Medium-O(N)-O(1))
```
###### Binary
```
Concept: Use "AND"(&), "OR"(|), "XOR"(^), "Bit Shift"(<< or >>)
Problem Types:
1. Result("XOR"(^)) and Carry("AND"(&)) for SUM problem. Example: 371. Sum of Two Integers (Easy-O(1)-O(1))
    - Other Skill: Restrict 32-bit number. Use "number & 0xffffffff".
2. Get 1st bit (mask 1) + Shift number. Example: 191. Number of 1 Bits (Easy-O(1)-O(1)) / 190. Reverse Bits
3. Use DP to count bits. Example: 338. Counting Bits (Easy-O(N)-O(N))
4. Two times "XOR"(^). Example: 268. Missing Number 
```

###### DP
```
Concept: Can divide into sub-problem.
Solution1: Use cache + recursion
Solution2: Use DP (Bottom-up)
Problem Types:
- Coin Changes. Example: 518. Coin Change II (Medium-O(M*N)-O(N))
```

###### Graph
```
Concept: Traverse graph nodes using DFS/BFS
Problem Types:
1. (DAG)Topo Order Visit. Example: course problem
2. Detect Unconneted. Example: Find Island Count
3. Detect Acyclic: Example: Graph Valid Tree
```


###### Interval
```
Concept: Overlap / Merge / Insert
Problem Types
1. Insert Interval (Check Overlap + Merge). Example: 57. Insert Interval (Medium-O(N)-O(N))
2. Merge Interval. Example: 56. Merge Intervals (Medium-O(N)-O(N))
3. Non-overlapping. Example: 435. Non-overlapping Intervals. (Medium-O(N)-O(N)) / 252. Meeting Rooms (Medium-O(N)-O(N))
4. Minimum Number of Meeting Rooms. Example: 253. Meeting Rooms II. (Medium-O(NlogN)-O(N))
```

###### Linked List
```
Problem Types:
1. Reverse. Example: 206. Reverse Linked List (Easy-O(N)-O(1))
2. Detect Cycle. Example: 141. Linked List Cycle. (Easy-O(N)-O(1))
3. Merge. Example: 21. Merge Two Sorted Lists (Easy-O(M+N)-O(M+N))
4. Merge K List. Example: 23. Merge k Sorted Lists (Hard-O(N * logK)-O(N*K))
5. Remove node. Example: 19. Remove Nth Node From End of List (Easy-O(N)-O(1))
6. Find Middle + Reverse + Merge. (in-place) Example: 143. Reorder List (Medium-O(N)-O(1))
```

###### Matrix
```
Problem Types:
1. Fill Zero. Example: 73. Set Matrix Zeroes (Medium-O(M*N)-O(1))
2. Spiral Matrix. Example: 54. Spiral Matrix (Medium-O(M*N)-O(M*N))
3. Metrix Rotate 90 Degree. Example: 48. Rotate Image (Medium-O(N*N)-O(1))
4. Word Search. (Back-tracking) Example: 79. Word Search. (Medium-O(M * N * 4^W)-O(W))
```


###### String
```
Concept: Sliding Window
Problem Types:
1. Example: 3. Longest Substring Without Repeating Characters. (Medium-O(N)-O(N))
2. Example: 424. Longest Repeating Character Replacement. (Medium-O(N)-O(1)) 
3. Example: 76. Minimum Window Substring. (Hard-O(N)-O(1)) 
4. Anagrams: Example: 242. Valid Anagram (Easy-O(N)-O(1)). / 49. Group Anagrams (Medium-O(M*N)-O(M))
5. Parentheses (open-close). Example: 20. Valid Parentheses (Easy-O(N)-O(N)) 
6. Palindrome. Example: 125. Valid Palindrome (Easy-O(N)-O(1)) / 5. Longest Palindromic Substring (Medium-O(N^2)-O(1)) / 647. Palindromic Substrings (Medium-O(N^2)-O(1))
7. Encode and Decode. Example: 271. Encode and Decode Strings. (Medium-O(N*W)-O(N*W))
```


###### Tree
```
Concept: DFS (preorder - inorder - postorder) / BFS / Trie
Problem Types:
1. Max Depth. Example: 104. Maximum Depth of Binary Tree (Easy-O(N)-O(1))
2. Compare is Same Tree. Example: 100. Same Tree (Easy-O(N)-O(1))
3. Invert Tree. Example: 226. Invert Binary Tree (Easy-O(N)-O(1))
4. Maximum Path Sum. Example: 124. Binary Tree Maximum Path Sum. (Hard-O(N)-O(H))
5. Tree Level Order Traversal. Example: 102. Binary Tree Level Order Traversal. (Medium-O(N)-O(N))
6. Serialize and Deserialize. Example: 297. Serialize and Deserialize Binary Tree (Hard-O(N)-O(N))
7. Same Tree / SubTree of another tree. Example: 572. Subtree of Another Tree. (Medium-O(M*N)-O(1))
8. Example: 105. Construct Binary Tree from Preorder and Inorder Traversal.(Medium-O(N^2)-O(1))
9. BST (Binary Search Tree). Example: 98. Validate Binary Search Tree. (Medium-O(N)-O(N)) / Example: 230. Kth Smallest Element in a BST. (Medium-O(N)-O(1)) / Example: 235. Lowest Common Ancestor of a Binary Search Tree. (Medium-O(logN)-O(1))
10. Trie. Example: 208. Implement Trie (Prefix Tree) / 211. Design Add and Search Words Data Structure / 212. Word Search II (Hard-O(4^(M*N)*Wlen)-O(W*Wlen))
```

###### Heap
```
Problem Types:
1. Example: 23. Merge k Sorted Lists. (Hard-O(N*logK)-O(logK))
2. Example: 347. Top K Frequent Elements. (Medium-O(N)-O(N))
3. Find Medium. Example: 295. Find Median from Data Stream. (Hard-O(logN)-O(N)) for addNum
```



# Beside Brind75
- 518. Coin Change II
- 39. Combination Sum