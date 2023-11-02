# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _dfs(self, root: TreeNode):
        left_sum = 0
        right_sum = 0

        if root.left:
            left_sum = max(0, self._dfs(root.left))
        if root.right:
            right_sum = max(0, self._dfs(root.right))

        self._max = max(self._max, (root.val + left_sum + right_sum))
        
        return (root.val + left_sum) if left_sum > right_sum else (root.val + right_sum)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._max = -1000
        self._dfs(root)
        return self._max
