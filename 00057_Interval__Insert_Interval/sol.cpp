#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
		
		intervals.push_back(newInterval);
		sort(intervals.begin(), intervals.end(), Solution::compare);
		
		int x = 0;
		for (int i = 1; i < intervals.size(); i++) {
			if (intervals[x][1] >= intervals[i][0]) {
				intervals[x][1] = max(intervals[x][1], intervals[i][1]);
			}
			else {
				x++;
				intervals[x] = intervals[i];
			}
		}
		
		vector<vector<int>> ans;
		for (int i = 0; i <= x; i++) {
			ans.push_back(intervals[i]);
		}
		return ans;
    }
	
	static bool compare(vector<int> i, vector<int> j) {
		return i[0] < j[0];
	}

};
