class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int s = 0;
        int e = nums.size() - 1;
        int m = 0;

        while (s <= e) {
            m = (s + e) / 2;

            if (nums[m] == target) {
                return m;
            }
            if (nums[s] == target) {
                return s;
            }
            if (nums[e] == target) {
                return e;
            }

            if (nums[m] >= nums[s]) {
                // s ~ m is ordered

                if (nums[s] <= target && target <= nums[m]) {
                    // target is between s ~ m
                    s++;
                    e = m - 1;
                }
                else {
                    // target is between m ~ e
                    s = m + 1;
                    e--;
                }
            }
            else {
                // m ~ e is ordered

                if (nums[m] <= target && target <= nums[e]) {
                    // target is between m ~ e
                    s = m + 1;
                    e--;
                }
                else {
                    // target is between s ~ m
                    s++;
                    e = m - 1;
                }

            }
        }

        return -1;

    }
};