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
```

###### Graph
```
Concept: Traverse graph nodes
Problem Types:
1. (DAG)Topo Order Visit. Example: course problem
2. Detect Unconneted. Example: Find Island Count
3. Detect Acyclic: Example: Graph Valid Tree
```


###### Interval
```
Problem Types
1. Insert Interval (Check Overlap + Merge)
```





