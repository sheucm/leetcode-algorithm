class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        // Binary Search

        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {

            int m = (l + r) / 2;
            int cnt = 0;

            for (int n : nums) {
                if (n <= m) {
                    cnt++;
                }
            }

            if (cnt <= m) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }


        return l;
    }
};