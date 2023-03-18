class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<bool> dp (nums.size());
        dp[nums.size() - 1] = true;

        for (int i = nums.size() - 2; i >= 0; i--) {
            int & max_steps = nums[i];
            bool can_reach = false;
            for (int j = i + 1; j <= i + max_steps; j++) {
                if (dp[j]) {
                    can_reach = true;
                    break;
                }
            }
            dp[i] = can_reach;
        }
        return dp[0];
    }
};