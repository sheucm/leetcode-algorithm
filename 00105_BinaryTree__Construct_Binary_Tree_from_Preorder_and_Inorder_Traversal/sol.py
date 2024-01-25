# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(1)
        if not preorder or not inorder: 
            return None
        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1+mid], inorder[:mid])
        root.right = self.buildTree(preorder[1+mid:], inorder[mid+1:])
        return root