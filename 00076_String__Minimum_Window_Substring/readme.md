
# Problem
https://leetcode.com/problems/minimum-window-substring/description/

# Skill
- Sliding Window
- Hash Table

# Challenges
(empty)

# Solving Mindset
1. Use two hash tables for `s` and `t`.
2. Build `t` hash table
3. Iterate `s` with sliding window, and update the `s` hash table.
4. Use `need, have` variables to see if match the requirement.
5. If match the requirement, update the `output` varaible.
6. Shink the window until `need, have` break the requirement.
7. Loop Step3~6 until the end of `s`.

# Complexity
Time: O(N)
Space: O(1)

# Reference
- https://www.youtube.com/watch?v=jSto0O4AJbM
