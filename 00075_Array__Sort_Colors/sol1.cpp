class Solution {
public:
    void sortColors(vector<int>& nums) {

        int idx_2 = nums.size() - 1;
        int idx_1 = -1;

        for (int i = 0; i <= idx_2; i++) {
            if (nums[i] == 0) {
                if (idx_1 != -1 && nums[idx_1] == 1) {
                    _swap(nums, idx_1++, i);
                }
            } else if (nums[i] == 2) {
                _swap(nums, i--, idx_2--);
            } else {
                if (idx_1 == -1) {
                    idx_1 = i;
                }
            }
        }
    }

private:
    void _swap(vector<int>& nums, int idx1, int idx2) {
        int temp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = temp;
    }
};