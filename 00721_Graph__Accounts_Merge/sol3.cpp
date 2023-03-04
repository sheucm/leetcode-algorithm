class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {

        // build graph
        unordered_map<string, vector<string>> adj;  // <email, adj_emails>

        for (auto & account : accounts) {

            for (int i = 1; i < account.size() - 1; i++) {
                string curr_email = account[i];
                string next_email = account[i + 1];
                
                adj[curr_email].push_back(next_email);
                adj[next_email].push_back(curr_email);
            }
        }


        vector<vector<string>> ans;
        unordered_map<string, bool> is_visit;    // <email, is_visit>
        for (auto & account : accounts) {
            string name = account[0];

            for (int i = 1; i < account.size(); i++) {
                if (is_visit[account[i]]) {
                    continue;
                }
                set<string> emails;     // will sort by default
                dfs(account[i], adj, is_visit, emails);

                vector<string> final_account {name};
                for (const auto & email: emails) {
                    final_account.push_back(email);
                }
                ans.push_back(final_account);
            }
        }


        return ans;
    }
private:
    void dfs(
        string curr_email,
        unordered_map<string, vector<string>>& adj,
        unordered_map<string, bool>& is_visit, // <email, is_visit>
        set<string>& emails
    ) {
        if (is_visit[curr_email]) {
            return;
        }

        is_visit[curr_email] = true;
        emails.insert(curr_email);

        for (string adj_email : adj[curr_email]) {
            dfs(adj_email, adj, is_visit, emails);
        }
    }
};