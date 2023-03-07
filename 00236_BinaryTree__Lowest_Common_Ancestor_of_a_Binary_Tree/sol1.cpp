/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

        vector<TreeNode*> path_p;
        vector<TreeNode*> path_q;

        _dfs(root, p, path_p);
        _dfs(root, q, path_q);

        int length = min(path_p.size(), path_q.size());
        TreeNode* ans = NULL;
        for (int i = length - 1; i >= 0; i--) {
            if (path_p[i] == path_q[i]) {
                ans = path_p[i];
                break;
            }
        }
        return ans;
    }

private:
    bool _dfs(
        TreeNode* curr_node,
        TreeNode* target,
        vector<TreeNode*>& path
    ) {
        if (!curr_node) return false;

        path.push_back(curr_node);
        if (curr_node == target) return true;

        if (_dfs(curr_node->left, target, path)) return true;
        if (_dfs(curr_node->right, target, path)) return true;

        path.erase(path.end() - 1);
        return false;
    }
};