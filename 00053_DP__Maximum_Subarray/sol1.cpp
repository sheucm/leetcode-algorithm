class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        int max_val = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            nums[i] = max(nums[i], nums[i-1] + nums[i]);
            if (nums[i] > max_val) {
                max_val = nums[i];
            }
        }
        return max_val;
    }
};