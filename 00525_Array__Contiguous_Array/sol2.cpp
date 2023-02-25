class Solution {
public:
    int findMaxLength(vector<int>& nums) {

        unordered_map<int, int> _seen;  // <sum, 1st idx of nums>

        int ans = 0;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += (nums[i] == 0 ? -1 : 1);

            if (sum == 0) {
                ans = max(ans, i + 1);
                continue;
            }

            if (_seen.count(sum)) {
                ans = max(ans, i - _seen[sum]);
            } else {
                _seen[sum] = i;
            }
        }
        return ans;
    }
};