class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> dfs_nums;
        _recur(nums, dfs_nums, ans);
        return ans;
    }
private:
    void _recur(
        vector<int>& nums,
        vector<int>& dfs_nums,
        vector<vector<int>>& ans
    ) {
        if (nums.size() == 1) {
            dfs_nums.push_back(nums[0]);
            ans.push_back(dfs_nums);
            dfs_nums.erase(dfs_nums.end() - 1);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {

            vector<int> next_nums (nums);
            next_nums.erase(next_nums.begin() + i);

            dfs_nums.push_back(nums[i]);
            _recur(
                next_nums, 
                dfs_nums,
                ans
            );
            dfs_nums.erase(dfs_nums.end() - 1);
        }
    }
};