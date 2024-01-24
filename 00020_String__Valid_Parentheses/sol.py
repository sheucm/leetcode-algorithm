class Solution:
    def isValid(self, s: str) -> bool:
        

        ### Solution: Stack
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        close2open = {')': '(', '}': '{', ']': '['}
        st = []
        for c in s:
            if c in close2open:
                if st and st[-1] == close2open[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False




                    
