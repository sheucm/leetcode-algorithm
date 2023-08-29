class Solution:

    def _dfs(
        self, 
        board: List[List[str]],
        x: int,
        y: int
    ):

        def _next():
            if x+1 < 9:
                return self._dfs(board, x+1, y)
            elif y+1 < 9:
                return self._dfs(board, 0, y+1)
            else:
                return True

        if board[x][y] != '.':
            return _next()
        
        else:
            exists = set()

            for i in range(9):
                if board[x][i] != '.':
                    exists.add(board[x][i])
                if board[i][y] != '.':
                    exists.add(board[i][y])
                
            block = [int(x/3), int(y/3)]
            for i in range(3):
                for j in range(3):
                    _x = 3 * block[0] + i
                    _y = 3 * block[1] + j
                    if board[_x][_y] != '.':
                        exists.add(board[_x][_y])
            
            for num in range(9):
                if f"{num+1}" not in exists:
                    board[x][y] = f"{num+1}"
                    if _next():
                        return True
                    board[x][y] = "."
            
            return False
                

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        return self._dfs(board, 0, 0)

