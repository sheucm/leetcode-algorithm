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
        _bfs(root, ans);
        return ans;
    }
private:
    void _bfs(
        TreeNode* root,
        vector<int>& ans
    ) {
        vector<TreeNode*> list;
        if (!root) return;
        list.push_back(root);
        while (list.size() > 0) {
            
            vector<TreeNode*> next_list;
            for (int i = 0; i < list.size(); i++) {
                TreeNode* node = list[i];
                if (i == 0) ans.push_back(node->val);
                if (node->right) next_list.push_back(node->right);
                if (node->left) next_list.push_back(node->left);
            }
            list = next_list;
        }
    }
};