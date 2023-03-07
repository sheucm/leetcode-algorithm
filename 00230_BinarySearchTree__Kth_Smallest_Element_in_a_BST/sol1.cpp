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
    int kthSmallest(TreeNode* root, int k) {
        int cnt = 0;
        int ans = -1;
        _dfs(root, cnt, ans, k);
        return ans;
    }

private:
    void _dfs(
        TreeNode* root,
        int & cnt,
        int & ans,
        int K
    ) {
        if (!root) return;

        _dfs(root->left, cnt, ans, K);
        if (ans != -1) return;

        if (++cnt == K) {
            ans = root->val;
            return;
        }

        _dfs(root->right, cnt, ans, K);
    }
};