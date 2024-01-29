from typing import List
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        comb_collection = defaultdict(lambda: defaultdict(set))
        DP = [[0] * (target+1) for _ in range(len(candidates)+1)]
        for r in range(len(candidates)+1):
            DP[r][-1] = 1
        for r in range(len(candidates)-1, -1, -1):
            for c in range(target-1, -1, -1):
                
                ### Handle Bottom One
                bottom_dp = DP[r+1][c]
                bottom_comb = comb_collection[r+1][c]
                
                ### Handle Right One
                right_dp = 0
                right_comb = set()
                if c + candidates[r] < (target+1):
                    right_dp = DP[r][c + candidates[r]]
                    right_comb = comb_collection[r][c + candidates[r]]
                
                ### Sum together
                DP[r][c] = bottom_dp + right_dp
                comb_collection[r][c] |= bottom_comb
                if right_dp > 0:
                    if right_comb:
                        for comb in right_comb:
                            comb_collection[r][c].add(tuple([candidates[r]] + list(comb)))
                    else:
                        comb_collection[r][c].add((candidates[r],))
                
                
        ans = [list(comb) for comb in comb_collection[0][0]]
        return ans
        
                    
