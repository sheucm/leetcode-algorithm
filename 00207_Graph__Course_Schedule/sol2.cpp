class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        vector<int> adj[n];
        for (auto pair : prerequisites) {
            adj[pair[0]].push_back(pair[1]);
        }

        vector<int> vis (n, 0);     // 0: todo / 1: on-going / 2: done
        for (int i = 0; i < n; i++) {
            if (is_circular(i, adj, vis)) {
                return false;
            }
        }
        return true;
    }
private:
    bool is_circular(
        int id,
        vector<int> adj[],
        vector<int>& vis
    ) {
        
        if (vis[id] == 1) {
            return true;
        }
        if (vis[id] == 0) {
            vis[id] = 1;
            for (auto pre_course : adj[id]) {
                if (is_circular(pre_course, adj, vis)) {
                    return true;
                }
            }
        }
        vis[id] = 2;
        return false;
    }
};