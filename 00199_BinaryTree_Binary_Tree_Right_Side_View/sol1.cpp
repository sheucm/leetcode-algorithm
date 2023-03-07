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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        int level = 0;
        _dfs(root, 0, level, ans);
        return ans;
    }
private:
    void _dfs(
        TreeNode* curr,
        int curr_level,
        int& level,
        vector<int>& ans
    ) {
        if (!curr) {
            return;
        }
        if (curr_level == level) {
            ans.push_back(curr->val);
            level++;
        }
        _dfs(curr->right, curr_level + 1, level, ans);
        _dfs(curr->left, curr_level + 1, level, ans);
    }
};