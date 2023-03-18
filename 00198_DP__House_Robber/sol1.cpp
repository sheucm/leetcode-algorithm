class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        vector<int> dp(nums.size(), -1);

        // Two start points
        int ans1 = _rob(nums, dp, nums.size() - 1);
        int ans2 = _rob(nums, dp, nums.size() - 2);

        return max(ans1, ans2);
    }
private:
    int _rob(vector<int>& nums, vector<int>& dp, int i) {
        int ret;
        if (i == 0 || i == 1) ret = nums[i];
        else if (i == 2) ret = nums[2] + nums[0];
        else if (dp[i] != -1) ret = dp[i];
        else ret = nums[i] + max(_rob(nums, dp, i - 2), _rob(nums, dp, i - 3));
        return dp[i] = ret;
    }
};