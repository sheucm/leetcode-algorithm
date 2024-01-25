# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(H)
        ans = root.val
        def dfs(v):
            nonlocal ans
            if not v: 
                return 0
            l = dfs(v.left)
            r = dfs(v.right)
            ans = max(ans, v.val + l + r)
            return v.val + max(0, l, r)
        dfs(root)
        return ans



