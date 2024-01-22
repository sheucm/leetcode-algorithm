
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ### Solution1: DFS
        ### Time Complexity: O(V + E)
        ### Space Complexity: O(V + E)
        graph = [set() for _ in range(numCourses)]
        for v1, v2 in prerequisites:
            graph[v1].add(v2)
        vis = [False] * numCourses
        cache = {}
        def dfs(v):
            if vis[v]:
                return False
            if not graph[v]:
                return True
            if v in cache:
                return cache[v]
            vis[v] = True
            ret = True
            for u in graph[v]:
                if not dfs(u):
                    ret = False
                    break
            vis[v] = False
            cache[v] = ret
            return ret
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        ### Solution2: BFS (Topo Order)
        ### Time Complexity: O(V + E)
        ### Space Complexity: O(V + E)
        # graph = [set() for _ in range(numCourses)]
        # in_degree = [0] * numCourses
        # for v1, v2 in prerequisites:
        #     graph[v2].add(v1) # Directed Graph
        #     in_degree[v1] += 1
        # q = [v for v in range(numCourses) if in_degree[v] == 0]
        # topo_order = []
        # while q:
        #     v = q.pop(0)
        #     topo_order.append(v)
        #     for u in graph[v]:
        #         in_degree[u] -= 1
        #         if in_degree[u] == 0:
        #             q.append(u)
        # return len(topo_order) == numCourses
            