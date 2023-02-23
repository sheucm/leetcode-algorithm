class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<vector<int>> diff_idx;
        int sum = 0;
        for (int i = 0; i < gas.size(); i++) {
            int diff = gas[i] - cost[i];
            diff_idx.push_back({diff, i});
            sum += diff;
        }

        if (sum < 0) {
            return -1;
        }

        sort(diff_idx.begin(), diff_idx.end(), greater< vector<int> >());

        int ans = -1;
        for (int i = 0; i < diff_idx.size(); i++) {
            auto obj = diff_idx[i];
            int diff = obj[0];
            int idx = obj[1];

            if (diff < 0) {
                break;
            }

            int ret = _start_journey(gas, cost, idx);
            if (ret != -1) {
                ans = ret;
                break;
            }
        }

        return ans;
    }


private:
    int _next(int idx, int size) {
        return (idx + 1) % size;
    }

    int _start_journey(vector<int>& gas, vector<int>& cost, const int start) {
        int j = start;
        int g = 0;
        do {
            g += gas[j];
            g -= cost[j];
            if (g >= 0) {
                // successfully arrived next station
                j = _next(j, gas.size());
                if (j == start) {
                    // complete travel around
                    return start;
                }
            } else {
                // failed
                break;
            }
        } while(true);
        return -1;
    }
};