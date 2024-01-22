class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        _map = [[0] * COLS for _ in range(ROWS)]


        ### Solution1: BFS
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(N*M)
        def search(r, c, land_id):
            if _map[r][c] > 0: return
            _map[r][c] = land_id
            dirs = [0,1,0,-1,0]
            for i in range(4):
                r2 = r + dirs[i]
                c2 = c + dirs[i+1]
                if (0 <= r2 < ROWS and 0 <= c2 < COLS):
                    if grid[r2][c2] == "1":
                        search(r2, c2, land_id)

        ### Solution1: DFS
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(N*M)
        # def search(r, c, land_id):
        #     if _map[r][c] > 0:
        #         return
        #     _map[r][c] = land_id
        #     dirs = [0,1,0,-1,0]
        #     for i in range(4):
        #         r2 = r + dirs[i]
        #         c2 = c + dirs[i+1]
        #         if (0 <= r2 < ROWS and 0 <= c2 < COLS):
        #             if grid[r2][c2] == "1":
        #                 search(r2, c2, land_id)


        land_id = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    land_id += 1
                    search(i, j, land_id)

        land_set = set()
        for i in range(ROWS):
            for j in range(COLS):
                if _map[i][j] != 0:
                    land_set.add(_map[i][j])
        return len(land_set)