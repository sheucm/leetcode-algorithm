class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        int _max = INT_MIN;
        _maxSubArray(nums, nums.size() - 1, _max);
        return _max;
    }
private:
    int _maxSubArray(vector<int>& nums, int i, int& _max) {
        int ans;
        if (i == 0) {
            ans = nums[i]; 
        }
        else {
            int sub = _maxSubArray(nums, i - 1, _max);
            ans = max(sub + nums[i], nums[i]);
        }
        _max = max(_max, ans);
        return ans;
    }
};