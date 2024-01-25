# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        max_depth = 0
        def dfs(v, d):
            nonlocal max_depth
            if not v:
                return
            max_depth = max(max_depth, d)
            dfs(v.left, d + 1)
            dfs(v.right, d + 1)
        dfs(root, 1)
        return max_depth


        ### Solution1: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        # def bfs(v):
        #     max_depth = 0
        #     q = [(1, v)]
        #     while q:
        #         d, v = q.pop(0)
        #         if not v: continue
        #         max_depth = max(max_depth, d)
        #         q.append((d+1, v.left))
        #         q.append((d+1, v.right))
        #     return max_depth
        # return bfs(root)