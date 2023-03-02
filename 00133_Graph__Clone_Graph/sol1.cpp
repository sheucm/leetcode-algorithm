/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {

        if (!node) {
            return NULL;
        }

        if (node->neighbors.size() == 0) {
            return new Node(node->val);
        }

        unordered_map<int, Node*> mp;
        return dfs(node, mp);
    }


private:
    Node* dfs(Node* curr, unordered_map<int, Node*>& mp) {

        Node* clone = new Node(curr->val);
        mp[curr->val] = clone;
        for (auto it : curr->neighbors) {
            if (mp.find(it->val) != mp.end()) {
                clone->neighbors.push_back(mp[it->val]);
            }
            else {
                clone->neighbors.push_back(dfs(it, mp));
            }
        }
        return clone;
    }
};