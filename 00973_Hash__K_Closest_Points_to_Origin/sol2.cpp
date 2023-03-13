class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        // Heap solution
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

        for (vector<int>& point : points) {
            int& x = point[0];
            int& y = point[1];
            int dis = pow(x, 2) + pow(y, 2);
            pq.push({ dis, x, y });
        }

        vector<vector<int>> ans;
        while (k--) {
            ans.push_back({ pq.top()[1], pq.top()[2] });
            pq.pop();
        }
        return ans;
    }
};