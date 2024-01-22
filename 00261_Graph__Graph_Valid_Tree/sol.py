class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [set() for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        vis = [False] * n
        path = [False] * n
        def dfs(v, pa = -1):
            if path[v]:
                return False
            if vis[v]:
                return True
            vis[v] = True
            path[v] = True
            for u in graph[v]:
                if u != pa:
                    if not dfs(u, v):
                        return False
            path[v] = False
            return True
        if not dfs(0):
            return False  # Have Circle Case
        if False in vis:
            return False  # Have Unconnected Case
        return True



        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # vis = [False] * n
        # def bfs(v):
        #     q = [(v, -1)]
        #     while q:
        #         v, pa = q.pop(0)
        #         if vis[v]:
        #             return False
        #         vis[v] = True
        #         for u in graph[v]:
        #             if u != pa:
        #                 q.append((u, v))
        #     return True
        # if not bfs(0):
        #     return False
        # if False in vis:
        #     return False
        # return True