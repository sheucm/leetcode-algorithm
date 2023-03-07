class Solution {
public:
    vector<int> findOrder(int N, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> next_courses (N, vector<int>());
        vector<int> indegree (N, 0);

        for (int i = 0; i < prerequisites.size(); i++) {
            next_courses[prerequisites[i][1]].push_back(prerequisites[i][0]);
            indegree[prerequisites[i][0]]++;
        }

        queue<int> q;
        for (int i = 0; i < N; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> ans;
        while (!q.empty()) {
            int curr = q.front(); q.pop();

            ans.push_back(curr);
            
            
            for (int next : next_courses[curr]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.push(next);
                }
                else if (indegree[next] < 0) {
                    cout << "Warn: indegree[" << next << "] is assert not to be less than 0." << endl;
                }
            }
            
        }

        if (ans.size() != N) {
            return {};
        }

        return ans;
    }
};