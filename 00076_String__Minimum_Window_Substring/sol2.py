class Solution:    

    def minWindow(self, s: str, t: str) -> str:

        sm, tm = {}, {}
        for ch in t:
            tm[ch] = 1 + tm.get(ch, 0)
        

        l = r = 0
        window = [0, 0]
        min_len = float('infinity')
        have, need = 0, len(tm)
        for idx in range(len(s)):

            ch = s[idx]
            sm[ch] = 1 + sm.get(ch, 0)
            if ch in tm and sm[ch] == tm[ch]:
                have += 1

            r = idx
            
            while have == need:
                
                if (r - l + 1) < min_len:
                    min_len = (r - l + 1)
                    window = [l, r]
                

                # move l point
                ch = s[l]
                sm[ch] -= 1
                if ch in tm and sm[ch] < tm[ch]:
                    have -= 1
                l += 1
        
        l, r = window
        if min_len == float('infinity'):
            return ""
        return s[l:r+1]

        
                


