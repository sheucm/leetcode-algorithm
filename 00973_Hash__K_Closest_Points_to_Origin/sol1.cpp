class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        vector<vector<int>> list;
        for (vector<int>& point : points) {
            int& x = point[0];
            int& y = point[1];
            int dis = pow(x, 2) + pow(y, 2);
            list.push_back({ dis, x, y });
        }

        sort(list.begin(), list.end());

        vector<vector<int>> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back({ list[i][1], list[i][2] });
        }
        return ans;
    }
};