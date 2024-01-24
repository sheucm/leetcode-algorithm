class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ### Solution1: Use (left-right-top-bottom) boundary
        ### Time Complexity: O(M*N)
        ### Space Complexity: O(M*N)
        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, COLS
        top, bottom = 0, ROWS
        ans = []
        while left < right and top < bottom:
            # Go right
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            # Go down
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            right -= 1

            # Check
            if (not left < right) or (not top < bottom): break

            # Go left
            for i in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][i])
            bottom -= 1

            # Go up
            for i in range(bottom-1, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans


        ### Solution1: Use VISITED flag
        ### Time Complexity: O(M*N)
        ### Space Complexity: O(M*N)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # DIRS = [0, 1, 0, -1, 0]
        # VISITED = 101
        # p = [0, 0]
        # ans = [matrix[0][0]]
        # matrix[0][0] = VISITED
        # while True:
        #     is_go = False
        #     for i in range(4):
        #         while (
        #             0 <= p[0] + DIRS[i] < ROWS and
        #             0 <= p[1] + DIRS[i+1] < COLS and
        #             matrix[p[0] + DIRS[i]][p[1]+ DIRS[i+1]] != VISITED
        #         ):
        #             p[0] += DIRS[i]
        #             p[1] += DIRS[i+1]
        #             ans.append(matrix[p[0]][p[1]])
        #             matrix[p[0]][p[1]] = VISITED
        #             is_go = True
        #     if not is_go: break
        # return ans
            
                 


