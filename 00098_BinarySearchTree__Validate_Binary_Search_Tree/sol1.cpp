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
    bool isValidBST(TreeNode* root) {
        
        auto ret = _dfs(root);
        if (ret.size() == 0) return false;
        return true;
    }
private:
    // return [min, max]
    vector<int> _dfs(
        TreeNode* curr
    ) {
        int MIN = curr->val;
        int MAX = curr->val;

        if (curr->left) {
            auto _ret = _dfs(curr->left);
            if (_ret.size() == 0) return {};
            int _min = _ret[0];
            int _max = _ret[1];
            if (_max >= curr->val) return {};
            if (_min < MIN) MIN = _min;
            if (_max > MAX) MAX = _max;
        }
        if (curr->right) {
            auto _ret = _dfs(curr->right);
            if (_ret.size() == 0) return {};
            int _min = _ret[0];
            int _max = _ret[1];
            if (_min <= curr->val) return {};
            if (_min < MIN) MIN = _min;
            if (_max > MAX) MAX = _max;
        }
        return {MIN, MAX};
    }
};