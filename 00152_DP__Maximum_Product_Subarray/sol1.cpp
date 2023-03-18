class Solution {
public:
    int maxProduct(vector<int>& nums) {

        unordered_map<int, pair<int, int>> dp; // [i] = {max, min}
        product(nums, dp, nums.size() - 1);
        int max_product = INT_MIN;
        for (auto p: dp) {
            if (p.second.first > max_product) {
                max_product = p.second.first;
            }
        }
        return max_product;
    }

private:
    pair<int,int> product(
        vector<int>& nums, 
        unordered_map<int, pair<int, int>>& dp,
        int i
    ) {
        if (i == 0) return dp[i] = pair<int, int>({nums[0], nums[0]});
        if (dp.find(i) != dp.end()) return dp[i];
        auto p = product(nums, dp, i-1);
        return dp[i] = pair<int, int>({
            max(
                nums[i],
                max(
                    nums[i] * p.first,
                    nums[i] * p.second
                )
            ),
            min(
                nums[i],
                min(
                    nums[i] * p.first,
                    nums[i] * p.second
                )
            )
        });
    }
};