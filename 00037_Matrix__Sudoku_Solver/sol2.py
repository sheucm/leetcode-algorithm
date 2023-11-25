class Solution:

    def _is_valid(self,
        n: str,
        i: int,
        j: int,
        board: List[List[str]],
    ) -> bool:

        # check + direction numbers
        for x in range(9):
            if x != j and board[i][x] == n:
                return False
            if x != i and board[x][j] == n:
                return False

        # check 3*3 block numbers
        block_i = int(i/3)
        block_j = int(j/3)

        for x in range(3):
            for y in range(3):
                _i = block_i * 3 + x
                _j = block_j * 3 + y
                if _i != i and _j != j and board[_i][_j] == n:
                    return False
        return True
            

    def _solve(self,
        i: int,
        j: int,
        board: List[List[str]]
    ) -> bool:
        if j >= 9:
            return self._solve(i+1, 0, board)
        if i >= 9:
            return True

        if board[i][j] != '.':
            return self._solve(i, j+1, board)
        

        for n in range(9):
            num = str(n+1)
            if self._is_valid(num, i, j, board):
                board[i][j] = num
                is_solved = self._solve(i, j+1, board)
                if is_solved:
                    return True
                board[i][j] = '.'
        return False

        


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._solve(0, 0, board)
        return None


        

