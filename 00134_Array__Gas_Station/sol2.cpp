class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        vector<int> diff;
        vector<int> idx_ref;
        for (int i = 0; i < gas.size(); i++) {
            int d = gas[i] - cost[i];
            if (
                i == 0
                || d < 0
                || (d >= 0 &&  diff[diff.size() - 1] < 0)
            ) {
                diff.push_back(d);
                idx_ref.push_back(i);
            } else {
                diff[diff.size() - 1] += d;
            } 
        }

        if (accumulate(diff.begin(), diff.end(), 0) < 0) {
            return -1;
        }

        // problem narrow to diff ary

        for (int i = 0; i < diff.size(); i++) {

            if (diff[i] < 0) {
                continue;
            }
            
            if (_start_journey(diff, i)) {
                return idx_ref[i];
            }
        }

        return -1;
    }


private:
    int _next(int idx, int size) {
        return (idx + 1) % size;
    }

    bool _start_journey(vector<int>& nums, const int start) {
        int sum = 0;
        int i = start;

        do {
            sum += nums[i];
            if (sum < 0) {
                return false;
            }

            i = _next(i, (int)nums.size());
        } while (i != start);

        return true;
    }
};