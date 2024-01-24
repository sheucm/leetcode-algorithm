class Solution:    

    def minWindow(self, S: str, T: str) -> str:

        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        window, countT = {}, {}

        for c in T:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        output, max_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(S)):
            c = S[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                # update answer
                if (r - l + 1) < max_len:
                    max_len = (r - l + 1)
                    output = [l, r]

                # shink window (pop left)
                window[S[l]] -= 1
                if S[l] in countT and countT[S[l]] > window[S[l]]:
                    have -= 1
                l += 1
        
        l, r = output
        return S[l: r+1] if max_len != float('inf') else ""

            

                

