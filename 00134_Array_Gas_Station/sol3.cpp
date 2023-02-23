class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        vector<int> diff;
        int ans = 0;
        for (int i = 0; i < gas.size(); i++) {
            int d = gas[i] - cost[i];

            if (
                i == 0
                || diff[diff.size() - 1] < 0
                || diff[diff.size() - 1] + d < 0
            ) {
                diff.push_back(d);
                ans = i;
            }
            else {
                diff[diff.size() - 1] += d;
            }

        }

        if (diff[diff.size() - 1] < 0) {
            return -1;
        }

        int sum = diff[diff.size() - 1];
        for (int i = 0; i < diff.size() - 1; i++) {
            sum += diff[i];
            if (sum < 0) {
                return -1;
            }
        }
        return ans;
    }

};