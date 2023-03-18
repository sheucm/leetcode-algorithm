class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        if (nums.size() == 1) return 1;

        // Greedy Method
        // Explanation: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
        vector<int> sub { nums[0] };

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > sub[sub.size() - 1]) {
                sub.push_back(nums[i]);
            }
            else {
                auto itr = lower_bound(sub.begin(), sub.end(), nums[i]);
                *itr = nums[i];
            }
        }

        return sub.size();
    }
};