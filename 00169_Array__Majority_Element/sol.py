from collections import Counter, defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ### Solution1
        counter = Counter(nums)
        li = [(cnt, num) for num, cnt in counter.items()]
        li.sort(reverse=True)
        return li[0][1]

        ### Solution2:
        # max_count = 0
        # max_num = -1
        # counter = defaultdict(int)
        # for n in nums:
        #     counter[n] += 1
        #     if counter[n] > max_count:
        #         max_count = counter[n]
        #         max_num = n
        # return max_num