class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [set() for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        island = [0] * n
        vis = [False] * n


        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        def traverse(v, _id):
            if vis[v]:
                return
            vis[v] = True
            island[v] = _id
            for u in graph[v]:
                traverse(u, _id)
        


        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # def traverse(v, _id):
        #     q = [v]
        #     while q:
        #         v = q.pop(0)
        #         if vis[v]:
        #             continue
        #         vis[v] = True
        #         island[v] = _id
        #         for u in graph[v]:
        #             q.append(u)



        land_id = 0
        for v in range(n):
            land_id += 1
            traverse(v, land_id)
        return len(set(island))