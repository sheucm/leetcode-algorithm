class Solution {
public:
    int maxProduct(vector<int>& nums) {

        vector<pair<int, int>> dp (nums.size());
        dp[0].first = dp[0].second = nums[0];

        int ans = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int _max = max(
                nums[i],
                max(
                    nums[i] * dp[i - 1].first,
                    nums[i] * dp[i - 1].second
                )
            );
            int _min = min(
                nums[i],
                min(
                    nums[i] * dp[i - 1].first,
                    nums[i] * dp[i - 1].second
                )
            );
            dp[i].first = _max;
            dp[i].second = _min;
            if (_max > ans) ans = _max;
        }
        return ans;
    }
};