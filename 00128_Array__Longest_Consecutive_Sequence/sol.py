class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for idx, n in enumerate(nums):
            m[n] = idx
        
        ### Solution1: DFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        vis = [False] * len(nums)
        def get_max_length(v):
            if vis[m[v]]:
                return 0
            vis[m[v]] = True
            length = 1
            if v+1 in m:
                length += get_max_length(v+1)
            if v-1 in m:
                length += get_max_length(v-1)
            return length



        ### Solution2: BFS
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # vis = [False] * len(nums)
        # def get_max_length(v):
        #     total_length = 0
        #     q = [v]
        #     while q:
        #         v = q.pop(0)
        #         if vis[m[v]]:
        #             continue
        #         vis[m[v]] = True
        #         total_length += 1
        #         if v+1 in m:
        #             q.append(v+1)
        #         if v-1 in m:
        #             q.append(v-1)
        #     return total_length



        max_length = 0
        for idx, n in enumerate(nums):
            max_length = max(max_length, get_max_length(n))
        return max_length