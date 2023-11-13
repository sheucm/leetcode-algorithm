class Solution:

    def _check_can_put_queen(self,
        queens: List[Tuple[int]],
        pos: Tuple[int]
    ) -> bool:

        for q in queens:

            # Check + direction
            if pos[0] == q[0] or pos[1] == q[1]:
                return False

            # Check X direction
            if abs(pos[0] - q[0]) == abs(pos[1] - q[1]):
                return False
        return True

    def _gen_ans(self,
        N: int,
        queens: List[Tuple[int]]
    ) -> List[List[str]]:
        res = []
        assert len(queens) == N
        for q in queens:
            j = q[1]
            row = "." * N
            row = row[:j] + 'Q' + row[j+1:]
            res.append(row)
        return res

    def _find2(self,
        N: int,
        ans: List[List[str]],
        queens: List[Tuple[int]] = [],
        level = 0,
    ) -> None:
        i = level
        for j in range(N):
            queen = (i, j)
            if self._check_can_put_queen(queens,queen):
                if level + 1 >= N:
                    # END
                    assert level + 1 == N
                    res = self._gen_ans(N, queens + [queen])
                    ans.append(res)
                else:
                    self._find2(N, ans, queens + [queen], level + 1)


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self._find2(n, ans = ans)
        return ans

