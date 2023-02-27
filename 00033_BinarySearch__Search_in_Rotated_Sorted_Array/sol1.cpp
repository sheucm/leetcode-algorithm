class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        if (nums.size() == 1) {
            return nums[0] == target ? 0 : -1;
        }

        // find pivot
        int i = nums.size() / 2;
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            if (nums[left] < nums[i]) {
                // pivot is between i ~ right
                left = i;
                i = (right + i) / 2;
            }
            else {
                // pivot is between left ~ i
                right = i;
                i = (left + i) / 2;
            }
        }
        const int pivot = i + 1;


        // search target
        i = nums.size() / 2;
        left = 0;
        right = nums.size() - 1;
        while(left <= right) {
            int idx = (i + pivot) % nums.size();
            int l_idx = (left + pivot) % nums.size();
            int r_idx = (right + pivot) % nums.size();
            if (nums[idx] == target) {
                return idx;
            }
            if (nums[l_idx] == target) {
                return l_idx;
            }
            if (nums[r_idx] == target) {
                return r_idx;
            }
            else if (target < nums[idx]) {
                // target is between left ~ i
                right = i - 1;
                left++;
                i = (left + i) / 2;
            }
            else {
                // target is between i ~ right
                left = i + 1;
                right--;
                i = (right + i) / 2;
            }
        }

        return -1;

    }
};