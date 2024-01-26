from collections import Counter
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ### Solution3: Hash Map + Bucket Sort
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, cnt in count.items():
            buckets[cnt].append(n)
        ans = []
        for i in range(len(buckets)-1, -1, -1):
            ans += buckets[i]
            if len(ans) >= k:
                break
        return ans
        


        ### Solution1: Hash Map + Sort
        ### Time Complexity: O(NlogN)
        ### Space Complexity: O(N)
        # count = Counter(nums)
        # li = [[v, k] for k, v in count.items()]
        # li.sort(reverse=True)
        # ans = [k for v, k in li[:k]]
        # return ans




        ### Solution2: Hash Map + Max Heap
        ### Time Complexity: O(NlogN)
        ### Space Complexity: O(N)
        # count = Counter(nums)
        # h = []
        # for n, cnt in count.items():
        #     heapq.heappush(h, (-cnt, n))
        # ans = []
        # for i in range(k):
        #     p = heapq.heappop(h)
        #     ans.append(p[1])
        # return ans