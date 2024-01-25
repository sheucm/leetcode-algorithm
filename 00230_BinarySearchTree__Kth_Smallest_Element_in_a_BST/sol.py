# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ### Solution: DFS in-order
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        ans, count = root.val, 0
        def dfs(v):
            nonlocal ans, count
            if not v: return False
            if dfs(v.left): return True

            count += 1
            if count == k:
                ans = v.val
                return True

            if dfs(v.right): return True
            return False
        dfs(root)
        return ans