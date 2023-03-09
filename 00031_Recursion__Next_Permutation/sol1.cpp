class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() == 1) return;
        if (!_next(0, nums)) sort(nums.begin(), nums.end());
        return;
    }

    bool _next(
        int idx,
        vector<int>& nums
    ) {
        if (idx == nums.size() - 2) {
            if (nums[idx] >= nums[idx + 1]) return false;
            swap(nums[idx], nums[idx + 1]);
            return true;
        }

        if (_next(idx + 1, nums)) {
            return true;
        }
        
        sort(nums.begin() + idx + 1, nums.end());
        for (int i = idx + 1; i < nums.size(); i++) {
            if (nums[i] > nums[idx]) {
                swap(nums[i], nums[idx]);
                return true;
            }
        }

        return false;
    }
};