/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> path;
        if (!root) return ans;
        _dfs(root, targetSum, path, ans);
        return ans;
    }
private:
    void _dfs(
        TreeNode* node,
        int targetSum,
        vector<int>& curr_path,
        vector<vector<int>>& paths
    ) {

        curr_path.push_back(node->val);

        if (!node->left && !node->right) {
            if (_sum(curr_path) == targetSum) {
                paths.push_back(curr_path);
            }
        }

        if (node->left) {
            _dfs(node->left, targetSum, curr_path, paths);
        }

        if (node->right) {
            _dfs(node->right, targetSum, curr_path, paths);
        }


        curr_path.erase(curr_path.end() - 1);
    }

    int _sum(vector<int>& list) {
        int ret = 0;
        for (int n : list) {
            ret += n;
        }
        return ret;
    }
};