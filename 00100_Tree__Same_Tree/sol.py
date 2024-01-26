# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        ### Solution3: DFS only
        ### Time Complexity: O(P+Q)
        ### Space Complexity: O(1)
        def dfs(v, u):
            if not v and not u: return True
            if not v or not u or v.val != u.val:  return False
            if not dfs(v.left, u.left):  return False
            if not dfs(v.right, u.right): return False
            return True
        return dfs(p, q)

        
        ### Solution1: DFS + output array
        ### Time Complexity: O(P+Q)
        ### Space Complexity: O(P+Q)
        # def dfs(v):
        #     if not v: 
        #         return [None]
        #     return [str(v.val)] + dfs(v.left) + dfs(v.right)
        # return dfs(p) == dfs(q)


        ### Solution2: BFS + output array
        ### Time Complexity: O(P+Q)
        ### Space Complexity: O(P+Q)
        # def bfs(v):
        #     q, res = [v], []
        #     while q:
        #         v = q.pop(0)
        #         if not v:
        #             res.append(None)
        #             continue
        #         res.append(v.val)
        #         q.append(v.left) 
        #         q.append(v.right)
        #     return res
        # return bfs(p) == bfs(q)