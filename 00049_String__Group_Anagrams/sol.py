from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Solution1: using only hash map
        ### Time Complexity: O(M * N)
        ### Space Complexity: O(M)
        m = defaultdict(list)
        for s in strs:
            counts = [0] * 26 # a ... z
            for c in s:
                counts[ord(c) - ord('a')] += 1
            m[tuple(counts)].append(s)
        return list(m.values())


        ### Solution1: using sort + hash map
        ### Time Complexity: O(M * NlogN)
        ### Space Complexity: O(M)
        # m = defaultdict(list)
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     m[sorted_s].append(s)
        # return list(m.values())
