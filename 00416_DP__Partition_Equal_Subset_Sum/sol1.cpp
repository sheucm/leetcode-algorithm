
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        

        int _sum = 0;
        for (int n : nums) _sum += n;
        if (_sum % 2 == 1) return false;
        int target = _sum / 2;

        vector<vector<int>> dp (nums.size(), vector<int>(target+1, -1));
        return isSubsetSum (nums, 0, target, dp);

    }
private:
    bool isSubsetSum (vector<int>& nums, int i, int target, vector<vector<int>>& dp) {
        if (target == 0) return true;
        if (i >= nums.size() || target < 0) return false;
        if (dp[i][target] != -1) return dp[i][target];
        return dp[i][target] = isSubsetSum(nums, i+1, target, dp) || isSubsetSum(nums, i+1, target - nums[i], dp);
    }
};