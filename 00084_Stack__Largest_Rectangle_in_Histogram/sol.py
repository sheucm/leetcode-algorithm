class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0
        st = []
        for x, y in enumerate(heights + [-1]):

            w = 0
            while st and st[-1][1] > y:
                pw, ph = st.pop(-1)
                w = w + pw
                res = max(res, w * ph)
            
            st.append([w + 1, y])
        return res

