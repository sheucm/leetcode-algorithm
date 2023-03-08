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
    int widthOfBinaryTree(TreeNode* root) {

        if (!root) return 0;        

        vector<pair<TreeNode*, long long>>list;     // <node, self-defined ID>   Node: left_child = 2*ID+1 | right_child = 2*ID+2
        list.push_back({root, 0});
        int max_width = 1;
        while (list.size() > 0) {

            vector<pair<TreeNode*, long long>> next_list;

            auto start_id = list[0].second;
            auto end_id = list[list.size() - 1].second;
            max_width = max(max_width, (int) (end_id - start_id + 1));
            
            for (auto& [node, curr_id] : list) {

                if (node->left) {
                    next_list.push_back({
                        node->left,
                        (curr_id - start_id) * 2 + 1
                    });
                }
                if (node->right) {
                    next_list.push_back({
                        node->right,
                        (curr_id - start_id) * 2 + 2
                    });
                }
            }
            list = next_list;
        }

        return max_width;
    }

};