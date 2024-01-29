class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        ROWS = len(image)
        COLS = len(image[0])

        path = set()
        start_color = image[sr][sc]
        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in path or
                image[r][c] != start_color
            ):
                return
            image[r][c] = color

            path.add((r, c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            path.remove((r, c))
        dfs(sr, sc)
        return image