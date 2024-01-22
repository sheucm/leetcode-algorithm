from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        indegree = {}
        graph = {}
        for w in words:
            for c in w:
                graph[c] = graph.get(c, set())
                indegree[c] = 0


        for i1, w1 in enumerate(words):
            for i2 in range(i1+1, len(words)):
                w2 = words[i2]
                if len(w1) > len(w2) and w1.startswith(w2):
                    return ""
                for c in range(min(len(w1), len(w2))):
                    if w1[c] != w2[c]:
                        if w2[c] not in graph[w1[c]]:
                            graph[w1[c]].add(w2[c])
                            indegree[w2[c]] += 1
                        break

        

        ### Solution1: BFS + Topo Order
        ### Time Complexity: O(W * W[i].length)
        ### Space Complexity: O(W * W[i].length)
        startings = [v for v in indegree if indegree[v] == 0]
        topo_order = []
        def bfs(v):
            q = [v]
            while q:
                v = q.pop(0)
                topo_order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        q.append(u)
        for v in startings:
            bfs(v)
        if len(topo_order) != len(graph):
            return ""
        return "".join(topo_order)





        ### Solution2: DFS + Post Order Visit
        ### Time Complexity: O(W * W[i].length)
        ### Space Complexity: O(W * W[i].length)
        # topo_order = []
        # vis = defaultdict(bool)
        # path = defaultdict(bool)
        # def dfs(v):
        #     if vis[v]:
        #         return True
        #     if path[v]:
        #         return False
        #     path[v] = True
        #     for u in graph[v]:
        #         if not dfs(u):
        #             return False
        #     topo_order.append(v)
        #     vis[v] = True
        #     path[v] = False
        #     return True

        # for v in graph:
        #     if not dfs(v):
        #         return ""
        
        # topo_order.reverse()
        # return "".join(topo_order)
