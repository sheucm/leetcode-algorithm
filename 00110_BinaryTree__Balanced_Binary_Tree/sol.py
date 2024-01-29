# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        ans = True
        def dfs(v, h):
            nonlocal ans
            if not v:
                return 0
            left_height = dfs(v.left, h+1)
            right_height = dfs(v.right, h+1)
            if abs(left_height - right_height) > 1:
                ans = False
            return 1 + max(left_height, right_height)
        dfs(root, 1)
        return ans