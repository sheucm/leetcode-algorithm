#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        

        int product_all = 1;
        auto ans = _init_ans(nums.size());
        vector<int> zero_index_coll;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                zero_index_coll.push_back(i);
            } else {
                product_all *= nums[i];
            }
        }

        if (zero_index_coll.size() > 1) {
            // all is zero
            return ans;
        }

        if (zero_index_coll.size() == 1) {
            // only 1 have value
            int zero_idx = zero_index_coll[0];
            ans[zero_idx] = product_all;
            return ans;
        }
        

        // no zero case
        for (int i = 0; i < nums.size(); i++) {
            ans[i] = product_all / nums[i];
        }
        
        return ans;
    }

private:
    vector<int> _init_ans(int size) {
        vector<int> ans;
        for (int i = 0; i < size; i++) {
            ans.push_back(0);
        }
        return ans;
    }
};





