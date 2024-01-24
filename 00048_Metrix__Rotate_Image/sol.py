class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ### Solution1: Boundary + Counter clock + Absoluate Point(Use offset concept)
        ### Time Complexity: O(N*N)
        ### Space Complexity: O(1)
        N = len(matrix)
        left, right = 0, N-1
        while left < right:
            top, bottom = left, right
            for i in range(right-left):
                topLeft = matrix[top][left+i]

                # Move bottom-left to top-left
                matrix[top][left+i] = matrix[bottom-i][left]
                # Move bottom-right to bottom-left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # Move top-right to bottom-right
                matrix[bottom][right-i] = matrix[top+i][right]
                # Move top-left to top-right (use topLeft)
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1



        ### Solution1: Boundary + Counter clock + Moving Points
        ### Time Complexity: O(N*N)
        ### Space Complexity: O(1)
        # N = len(matrix)
        # left, right = 0, N-1
        # while left < right:
        #     top = left
        #     for c in range(left, right):
        #         i, j = top, c
        #         topLeft = matrix[i][j]
        #         for idx in range(4):
        #             if idx == 3:
        #                 matrix[i][j] = topLeft
        #             else:
        #                 # Counter clock: (i, j) -> (j, N-1-i)
        #                 matrix[i][j] = matrix[N-1-j][i] 
        #                 i, j = N-1-j, i
        #     left += 1
        #     right -= 1


