"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        

        ### BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # if not node:
        #     return None
        # new_root = Node(node.val)
        # m = {}
        # m[new_root.val] = new_root
        # vis = defaultdict(bool)
        # q = [(node, new_root)]
        # while q:
        #     old_v, new_v = q.pop(0)
        #     if vis[old_v.val]:
        #         continue
        #     vis[old_v.val] = True
        #     for old_ch in old_v.neighbors:
        #         if vis[old_ch.val]:
        #             continue
        #         if old_ch.val in m:
        #             new_ch = m[old_ch.val]
        #         else: # New node
        #             new_ch = Node(old_ch.val)
        #             m[new_ch.val] = new_ch
        #         new_ch.neighbors.append(new_v)
        #         new_v.neighbors.append(new_ch)
        #         q.append((old_ch, new_ch))
        # return new_root


        ### DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        if not node:
            return None
        new_root = Node(node.val)
        m = {}
        m[new_root.val] = new_root
        vis = defaultdict(bool)
        def dfs(old_v, new_v):
            if vis[old_v.val]:
                return
            vis[old_v.val] = True
            for old_ch in old_v.neighbors:
                # Get new_ch
                if old_ch.val in m:
                    new_ch = m[old_ch.val]
                else:
                    new_ch = Node(old_ch.val)
                    m[new_ch.val] = new_ch
                new_v.neighbors.append(new_ch)
                dfs(old_ch, new_ch)
        dfs(node, new_root)
        return new_root