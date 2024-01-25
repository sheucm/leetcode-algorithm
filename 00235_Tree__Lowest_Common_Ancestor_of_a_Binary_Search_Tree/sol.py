# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ### Solution: DFS + BST Boundary
        ### Time Complexity: O(logN)
        ### Space Complexity: O(1)
        while root:
            if q.val < root.val and p.val < root.val:
                root = root.left
            elif q.val > root.val and p.val > root.val:
                root = root.right
            else:
                return root
        return None
        
