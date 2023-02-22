class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        auto ans = vector<int>(nums);

        for (int i  = 1; i < nums.size(); i++) {
            ans[i] = ans[i - 1] * nums[i];
        }

        int suf = 1;
        for (int j = nums.size() - 1; j >= 0; j--) {
            int pre = j == 0? 1 : ans[j - 1];
            ans[j] = pre * suf;
            suf *= nums[j];
        }

        return ans;
    }

};