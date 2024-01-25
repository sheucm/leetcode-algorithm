# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ### Solution: DFS + Boundary
        ### Time Complexity: O(N)
        ### Space Complexity: O(H)
        def dfs(v, b_min, b_max):
            if not v:
                return True
            if not (b_min < v.val < b_max):
                return False
            return (dfs(v.left, b_min, v.val) and 
                    dfs(v.right, v.val, b_max))
        return dfs(root, -float('inf'), float('inf'))
        