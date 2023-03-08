class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        ans.push_back({});

        for (int curr_num : nums) {
            vector<vector<int>> new_ans;
            for (auto subset : ans) {
                subset.push_back(curr_num);
                new_ans.push_back(subset);
            }
            ans.insert(ans.end(), new_ans.begin(), new_ans.end());
        }
        return ans;
    }

};