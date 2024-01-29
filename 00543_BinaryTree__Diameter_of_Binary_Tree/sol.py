# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        max_diameter = 0
        def dfs(v):
            nonlocal max_diameter
            if not v:
                return 0
            
            l = dfs(v.left)
            r = dfs(v.right)
            max_diameter = max(max_diameter, l + r)
            return 1 + max(l, r)
        dfs(root)
        return max_diameter