class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        vector<int> diff;
        int ans = 0;
        int sum = 0;
        for (int i = 0; i < gas.size(); i++) {
            int d = gas[i] - cost[i];
            sum += d;

            if (i == 0 || diff[diff.size() - 1] < 0) {
                diff.push_back(d);
                ans = i;
            }
            else {
                diff[diff.size() - 1] += d;
            }
        }

        if (diff[diff.size() - 1] < 0 || sum < 0) {
            return -1;
        }
        return ans;
    }

};