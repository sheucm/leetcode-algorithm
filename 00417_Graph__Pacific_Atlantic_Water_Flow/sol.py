class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ### Solution: BFS
        # ROWS = len(heights)
        # COLS = len(heights[0])
        # p_map = [[False] * COLS for _ in range(ROWS)] 
        # a_map = [[False] * COLS for _ in range(ROWS)]
        # pacific_starts = []
        # atlantic_starts = []
        # for j in range(COLS):
        #     pacific_starts.append((0, j))
        #     atlantic_starts.append((ROWS-1, j))
        # for i in range(ROWS):
        #     pacific_starts.append((i, 0))
        #     atlantic_starts.append((i, COLS-1))

        # def bfs(r, c, _map):
        #     q = [(r, c)]
        #     while q:
        #         r, c = q.pop(0)
        #         if _map[r][c]: continue
        #         _map[r][c] = True

        #         dirs = [0, 1, 0, -1, 0]
        #         for i in range(4):
        #             r2 = r + dirs[i]
        #             c2 = c + dirs[i+1]
        #             if (0 <= r2 < ROWS and 0 <= c2 < COLS):
        #                 if heights[r2][c2] >= heights[r][c]:
        #                     q.append((r2, c2))
                

        # for v in pacific_starts:
        #     bfs(v[0], v[1], p_map)

        # for v in atlantic_starts:
        #     bfs(v[0], v[1], a_map)
        
        # ans = []
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if p_map[i][j] and a_map[i][j]:
        #             ans.append([i, j])
        # return ans


        ### Solution: DFS
        ### Time Complexity: O(M * N)
        ### Space Complexity: O(M * N)
        ROWS = len(heights)
        COLS = len(heights[0])
        p_map = [[False] * COLS for _ in range(ROWS)] 
        a_map = [[False] * COLS for _ in range(ROWS)]
        
        pacific_starts = []
        atlantic_starts = []
        for j in range(COLS):
            pacific_starts.append((0, j))
            atlantic_starts.append((ROWS-1, j))
        for i in range(ROWS):
            pacific_starts.append((i, 0))
            atlantic_starts.append((i, COLS-1))





        ### Solution1: DFS
        ### Time Complexity: O(M * N)
        ### Space Complexity: O(M * N)
        def dfs(r, c, _map):
            if _map[r][c]: return
            _map[r][c] = True
            dirs = [0, 1, 0, -1, 0]
            for i in range(4):
                r2 = r + dirs[i]
                c2 = c + dirs[i+1]
                if (0 <= r2 < ROWS and 0 <= c2 < COLS):
                    if heights[r2][c2] >= heights[r][c]:
                        dfs(r2, c2, _map)
        for v in pacific_starts:
            dfs(v[0], v[1], p_map)
        for v in atlantic_starts:
            dfs(v[0], v[1], a_map)



        ### Solution1: BFS
        # def bfs(r, c, _map):
        #     q = [(r, c)]
        #     while q:
        #         r, c = q.pop(0)
        #         if _map[r][c]: continue
        #         _map[r][c] = True
        #         dirs = [0, 1, 0, -1, 0]
        #         for i in range(4):
        #             r2 = r + dirs[i]
        #             c2 = c + dirs[i+1]
        #             if (0 <= r2 < ROWS and 0 <= c2 < COLS):
        #                 if heights[r2][c2] >= heights[r][c]:
        #                     q.append((r2, c2))
        # for v in pacific_starts:
        #     bfs(v[0], v[1], p_map)
        # for v in atlantic_starts:
        #     bfs(v[0], v[1], a_map)
        
        



        ans = []
        for i in range(ROWS):
            for j in range(COLS):
                if p_map[i][j] and a_map[i][j]:
                    ans.append([i, j])
        return ans