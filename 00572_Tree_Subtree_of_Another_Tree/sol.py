# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def serialize(self, root):
        res = []
        def dfs(v):
            if not v:
                res.append("'N'")
                return
            res.append(f"'{v.val}'")
            dfs(v.left)
            dfs(v.right)
        dfs(root)
        return ','.join(res)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        ### Solution1 : Serialize
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(N+M)
        # root_ser = self.serialize(root)
        # sub_ser = self.serialize(subRoot)
        # return sub_ser in root_ser


        ### Solution2 : DFS
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(1)
        def same_tree(v1, v2):
            if not v1 and not v2: return True
            if not v1 or not v2: return False
            if v1.val != v2.val: return False
            return same_tree(v1.left, v2.left) and same_tree(v1.right, v2.right)
        if not root: return False
        if same_tree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
