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
    vector<vector<int>> levelOrder(TreeNode* root) {

        vector<TreeNode*> list;
        vector<vector<int>> ans;

        if (!root) return {};
        list.push_back(root);
        while(list.size() != 0) {
            vector<TreeNode*> next_level_list;
            vector<int> l;
            for (TreeNode* node : list) {
                l.push_back(node->val);
                if (node->left) next_level_list.push_back(node->left);
                if (node->right) next_level_list.push_back(node->right);
            }
            ans.push_back(l);
            list = next_level_list;
        }
        return ans;
    }
};