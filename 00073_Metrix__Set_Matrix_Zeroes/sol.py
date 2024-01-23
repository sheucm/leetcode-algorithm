class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ### Solution3:
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        r0, c0 = False, False
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0: r0 = True
                    if j == 0: c0 = True
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0
        for j in range(1, COLS):
            if matrix[0][j] == 0:
                for i in range(1, ROWS):
                    matrix[i][j] = 0
        if r0:
            for j in range(COLS):
                matrix[0][j] = 0
        if c0:
            for i in range(ROWS):
                matrix[i][0] = 0


        ### Solution2:
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(N+M)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # r_set = set()
        # c_set = set()
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             r_set.add(i)
        #             c_set.add(j)
        # for r in r_set:
        #     for j in range(COLS):
        #         matrix[r][j] = 0
        # for c in c_set:
        #     for i in range(ROWS):
        #         matrix[i][c] = 0

        ### Solution1:
        ### Time Complexity: O(N*M)
        ### Space Complexity: O(N*M)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # coll = []
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             coll.append((i, j))
        # for i, j in coll:
        #     for r in range(ROWS):
        #         matrix[r][j] = 0
        #     for c in range(COLS):
        #         matrix[i][c] = 0
        