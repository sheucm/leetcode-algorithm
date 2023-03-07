class Solution {
public:
    vector<int> findOrder(int N, vector<vector<int>>& p) {
        
        vector<vector<int>> G (N);
        vector<int> indegree (N);
        vector<int> ans;

        for (int i = 0; i < p.size(); i++) {
            G[p[i][1]].push_back(p[i][0]);
            indegree[p[i][0]]++;
        }

        for (int i = 0; i < N; i++) {
            if (indegree[i] == 0) {
                _dfs(i, N, G, indegree, ans);
            }
        }
        

        if (ans.size() != N) {
            return {};
        }

        return ans;
    }
private:
    void _dfs(
        int course,
        int N,
        vector<vector<int>>& G,
        vector<int>& indegree,
        vector<int>& ans
    ) {
        ans.push_back(course);
        indegree[course] = -1;  // mark as visited
        for (int next: G[course]) {
            if (--indegree[next] == 0) {
                _dfs(next, N, G, indegree, ans);
            }
        }
    }
};