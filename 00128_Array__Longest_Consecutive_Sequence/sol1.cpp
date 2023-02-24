class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        if (nums.size() == 0) {
            return 0;
        }

        sort(nums.begin(), nums.end());

        vector<int> nums2;
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                nums2.push_back(nums[i]);
            }
        }

        int ans = 1;
        int len = 1;
        for (int i = 1; i < nums2.size(); i++) {
            if (nums2[i] == nums2[i-1] + 1) {
                len++;
            } else {
                len = 1;
            }

            if (len > ans) {
                ans = len;
            }
        }
        return ans;
    }
};