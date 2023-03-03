class Node {
public:
    string name;
    string email;
    unordered_map<string, Node*> neighbors;  // <email, flag>

    Node() {
        name = "";
        email = "";
    }
    Node(string _name, string _email) {
        name = _name;
        email = _email;
    }

    void add_neighbor(Node* node) {
        neighbors[node->email] = node;
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {

        if (accounts.size() == 0) {
            return vector<vector<string>>();
        }

        // build graph
        unordered_map<string, Node*> m;     // <email, node>
        for (auto& account : accounts) {
            string name = account[0];
            Node* pre_node = NULL;;
            for (int i = 1; i < account.size(); i++) {
                string email = account[i];
                Node* curr_node = NULL;

                if (m.find(email) == m.end()) {
                    curr_node = new Node(name, email);
                    m[email] = curr_node;
                }
                else {
                    curr_node = m[email];
                }


                if (i != 1) {
                    curr_node->add_neighbor(pre_node);
                    pre_node->add_neighbor(curr_node);
                }
                
                pre_node = curr_node;
            }
        }

        vector<vector<string>> ans;
        unordered_map<string, bool> is_visit;   // <email, is_visit>
        for (auto & ptr : m) {
            auto & node = ptr.second;
            if (is_visit[node->email]) {
                continue;
            }

            set<string> emails;
            dfs(node, is_visit, emails);


            vector<string> account {node->name};
            for (const string& email : emails) {
                account.push_back(email);
            }
            sort(account.begin() + 1, account.end());
            ans.push_back(account);
        }


        return ans;
    }
private:
    void dfs(
        Node* node, 
        unordered_map<string, bool>& is_visit, // <email, is_visit>
        set<string>& emails
    ) {
        // cout << "dfs() node name=" << node->name << ", email=" << node->email << endl;

        if (is_visit[node->email]) {
            return;
        }

        is_visit[node->email] = true;
        emails.insert(node->email);

        for (auto & ptr : node->neighbors) {
            Node* neighbor = ptr.second;
            dfs(neighbor, is_visit, emails);
        }
    }
};