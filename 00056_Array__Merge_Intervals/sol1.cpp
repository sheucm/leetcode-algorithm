class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        int idx = 0;
        for (int i = 1; i < intervals.size(); i++) {
            auto& curr = intervals[idx];

            if (intervals[i][0] <= curr[1]) {
                // nned to merge
                curr[1] = max(curr[1], intervals[i][1]);
            } else {
                idx++;
                intervals[idx] = intervals[i];
            }
        }

        vector<vector<int>> ans;
        for (int i = 0; i <= idx; i++) {
            ans.push_back(intervals[i]);
        }
        return ans;

    }
};