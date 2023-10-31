class Solution:

    def get_steps(
        self,
        matrix: List[List[int]], 
        steps: List[List[int]], 
        i: int,  # |
        j: int,  # --
    ) -> int:
        if steps[i][j] > 0:
            return steps[i][j]
        
        TRAVELED_FLAG = -1
        steps[i][j] = TRAVELED_FLAG
        max_step_cnt = 1
        dirs = [0, -1, 0, 1, 0] # up down left right
        for x in range(4):
            ne = (i + dirs[x], j + dirs[x+1])
            if (
                ne[0] >= 0 and ne[0] < len(matrix)
                and ne[1] >= 0 and ne[1] < len(matrix[0])
                and steps[ne[0]][ne[1]] != TRAVELED_FLAG
                and matrix[ne[0]][ne[1]] > matrix[i][j]
            ):
                # can go next step
                _steps_cnt = 1 + self.get_steps(matrix, steps, ne[0], ne[1])
                max_step_cnt = max(max_step_cnt, _steps_cnt)

        steps[i][j] = max_step_cnt
        return max_step_cnt
 

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        y_len = len(matrix)
        x_len = len(matrix[0])

        steps = [[0] * x_len for i in range(y_len)]
        _ans = 0
        for i in range (y_len):
            for j in range(x_len):
                _steps = 0
                if steps[i][j] == 0:
                    _steps = self.get_steps(
                        matrix, 
                        steps, 
                        i,
                        j,
                    )
                else:
                    _steps = steps[i][j]
                _ans = max(_ans, _steps)
        return _ans
