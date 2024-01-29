class Solution:
    def trap(self, height: List[int]) -> int:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        st = []
        total_water = 0
        for w, h in enumerate(height):
            if not st or h < st[-1][1]:
                st.append((w, h))
                continue
            low = 0
            while st and h >= st[-1][1]:
                p_w, p_h = st.pop()
                total_water += (w - p_w - 1) * (min(h, p_h) - low)
                low = min(h, p_h)
            if st:
                total_water += (w - st[-1][0] - 1) * (min(h, st[-1][1]) - low)
            st.append((w, h))
        return total_water


                