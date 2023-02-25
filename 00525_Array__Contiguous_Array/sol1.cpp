class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        
        // Idx: sum and Val: index of nums
        // sum in (-nums.size() ~ -1) ===> store in index of (0 ~ nums.size() -1)
        // 0 ===> store in index of (nums.size())
        // sum in (1 ~ nums.size()) ===> store in index of (nums.size() + 1 ~ nums.size() * 2)
        vector<int> _map(nums.size() * 2 + 1, INT_MIN);

        int ans = 0;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += (nums[i] == 0 ? -1 : 1);

            if (sum == 0) {
                ans = max(ans, i + 1);
                continue;
            }

            int& idx_of_the_sum = _map[sum + nums.size()];
            if (idx_of_the_sum >= 0) {
                ans = max(ans, i - idx_of_the_sum);
            } else {
                idx_of_the_sum = i;
            }
        }

        return ans;
    }

};