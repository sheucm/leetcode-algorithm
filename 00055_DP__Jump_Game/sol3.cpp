class Solution {
public:
    bool canJump(vector<int>& nums) {
        int idx = nums.size() - 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (i + nums[i] >= idx) {
                idx = i;
            }
        }
        return idx == 0;
    }
};