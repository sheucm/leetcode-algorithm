class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int _min = nums[0];
        int _max = nums[0];
        int ans = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) swap(_min, _max);
            _min = min(nums[i], _min * nums[i]);
            _max = max(nums[i], _max * nums[i]);
            ans = max(ans, _max);
        }
        return ans;
    }
};