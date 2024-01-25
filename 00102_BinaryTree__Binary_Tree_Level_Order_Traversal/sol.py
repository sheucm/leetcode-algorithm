# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ### Solution: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        ans = defaultdict(list)
        def bfs(v):
            q = [(v, 0)]
            while q:
                v, level = q.pop(0)
                if not v: continue
                ans[level].append(v.val)
                q.append((v.left, level+1))
                q.append((v.right, level+1))
        bfs(root)
        return list(ans.values())