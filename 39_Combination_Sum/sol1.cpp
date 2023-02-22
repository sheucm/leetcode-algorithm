class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        return _solve(candidates, 0, target);
    }

private:
    vector<vector<int>> _solve(vector<int>& candidates, int idx, int target) {

        if (idx >= candidates.size() || target == 0) {
            return vector<vector<int>>();
        }

        int num = candidates[idx];
        int chosen_times = target / num;

        vector<vector<int>> ans;
        for (int i = 0; i <= chosen_times; i++) {

            vector<int> comb_sub1;
            for (int j = 0; j < i; j++) {
                comb_sub1.push_back(num);
            }

            int remain_num = target - num * i;

            if (remain_num == 0) {
                ans.push_back(comb_sub1);
                continue;
            }

            auto comb_sub2 = _solve(candidates, idx + 1, remain_num);
            for (int j = 0; j < comb_sub2.size(); j++) {

                auto& comb = comb_sub2[j];
                comb.insert(comb.end(), comb_sub1.begin(), comb_sub1.end());

                ans.push_back(comb);
            }
        }
        return ans;
    }
};