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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int N = preorder.size();
        TreeNode* root = new TreeNode();
        _search(root, 0, 0, N, preorder, inorder);
        return root;
    }

private:
    void _search(
        TreeNode* root,
        int pre_start,
        int in_start,
        int N,
        vector<int>& preorder, 
        vector<int>& inorder
    ) {
        int root_val = preorder[pre_start];
        root->val = root_val;

        // left
        int root_idx = -1;
        for (int i = in_start; i < in_start + N; i++) {
            if (inorder[i] == root_val) {
                root_idx = i;
                break;
            }
        }
        if (root_idx == -1) cout << "Warn: root_idx assert not to be -1." << endl;

        int left_num = root_idx - in_start;
        int right_num = N - 1 - left_num;

        if (left_num > 0) {
            root->left = new TreeNode();
            _search(
                root->left, 
                pre_start + 1, 
                in_start,
                left_num,
                preorder, 
                inorder
            );
        }
        

        if (right_num > 0) {
            root->right = new TreeNode();
            _search(
                root->right, 
                pre_start + 1 + left_num,
                root_idx + 1, 
                right_num,
                preorder, 
                inorder
            );
        }
        
    }


};