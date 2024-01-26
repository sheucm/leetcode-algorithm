# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ### Solution3: DFS. (without any extra memory)
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        def dfs(v):
            if not v:
                return None
            l, r = v.left, v.right
            v.left = dfs(r)
            v.right = dfs(l)
            return v
        return dfs(root)


        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # def dfs(v):
        #     if not v:
        #         return None
        #     root = TreeNode(
        #         val = v.val,
        #         left = dfs(v.right),
        #         right = dfs(v.left)
        #     )
        #     return root
        # return dfs(root)


        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # def bfs(v):
        #     if not v: return None
        #     root = TreeNode()
        #     q = [(v, root)]
        #     while q:
        #         v, new_v = q.pop(0)
        #         if not v:
        #             continue
        #         new_v.val = v.val
        #         if v.left:
        #             new_v.right = TreeNode()
        #             q.append((v.left, new_v.right))
        #         if v.right:
        #             new_v.left = TreeNode()
        #             q.append((v.right, new_v.left))
        #     return root
        # return bfs(root)
                