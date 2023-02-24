class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        int ans = 0;
        int minus_gas = 0;
        int rest_gas = 0;
        for (int i = 0; i < gas.size(); i++) {

            if (i == 0 || rest_gas < 0) {
                minus_gas += rest_gas;
                rest_gas = gas[i] - cost[i];
                ans = i;
            }
            else {
                rest_gas += gas[i] - cost[i];
            }
        }

        if (minus_gas + rest_gas < 0) {
            return -1;
        }
        return ans;
    }

};