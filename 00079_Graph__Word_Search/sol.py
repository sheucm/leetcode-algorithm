class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        ### Solution: Backtracking with DFS (Brute Force)
        ### Time Complexity: O(M * N * 4^W)
        ### Space Complexity: O(W)
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, idx):
            if idx == len(word): return True
            if (
                r < 0 or r >= ROWS or c < 0 or c >= COLS or
                board[r][c] != word[idx] or
                (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r+1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c-1, idx+1)
            )
            path.remove((r, c)) # Back tracking
            return res
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0): return True
        return False
        