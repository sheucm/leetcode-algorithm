
# Problem
https://leetcode.com/problems/alien-dictionary/description/

# Skill
- Topo Sort by using BFS/DFS

# Challenges
(empty)

# Solving Mindset
1. Transform problem to graph
2. Solved by DFS/BFS with topo order;

# Complexity
Time: O(W * W[i].length)
Space: O(W * W[i].length)

# Reference
https://www.youtube.com/watch?v=6kTZYvNNyps




# Problem Description (Hard)
(Note: For review usage, if there are any copyright issues, please let me know.)

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.


Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.