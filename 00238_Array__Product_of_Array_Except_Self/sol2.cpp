#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        auto pre = _get_pre(nums);
        auto suf = _get_suf(nums);

        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            int pre_v = i ? (pre[i-1]) : 1;
            int suf_v = (i < (nums.size() - 1))? suf[i+1] : 1;
            ans.push_back(
                pre_v * suf_v
            );
        }


        return ans;
    }
private:

    vector<int> _get_pre(vector<int>& nums) {
        auto pre = vector<int>(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            pre[i] = i ? nums[i] * pre[i-1] : nums[i];
        }
        return pre;
    }
    vector<int> _get_suf(vector<int>& nums) {
        auto suf = vector<int>(nums.size());
        for (int i = nums.size() - 1; i >= 0; i--) {
            suf[i] = (i < (nums.size() - 1))? nums[i] * suf[i+1] : nums[i];
        }
        return suf;
    }
};