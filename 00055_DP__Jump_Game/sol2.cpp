class Solution {
public:
    bool canJump(vector<int>& nums) {

        int idx = nums.size() - 1;

        while (idx >= 0) {
            if (idx == 0)  return true;

            int last_idx = -1;
            for (int step = 1; idx - step >= 0; step++) {
                int curr = idx - step;
                if (nums[curr] >= step) {
                    last_idx = curr;
                }
            }

            if (last_idx == -1) return false;
            idx = last_idx;
        }

        return false;
    }
};