#include <cmath>
using namespace std;

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        

        if (mat.size() == 0) {
            return vector<vector<int>> (mat.size(), vector<int>(mat[0].size(), 0));
        }

        vector<vector<int>> ans (mat.size(), vector<int>(mat[0].size(), INT_MAX));
        vector<pair<int, int>> zeros;
        vector<pair<int, int>> non_zeros;

        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[i].size(); j++) {
                if (mat[i][j] == 0) {
                    zeros.push_back(pair<int, int>(i, j));
                    ans[i][j] = 0;
                }
                else {
                    non_zeros.push_back(pair<int, int>(i, j));
                }
            }
        }

        for (int k = 0; k < non_zeros.size(); k++) {
            int i = non_zeros[k].first;
            int j = non_zeros[k].second;
            ans[i][j] = get_step(i, j, zeros);
        }


        return ans;
    }

private:
    int get_step(
        int i,
        int j,
        vector<pair<int, int>>& zeros
    ) {
        
        int step = INT_MAX;
        for (int k = 0; k < zeros.size(); k++) {
            int zero_i = zeros[k].first;
            int zero_j = zeros[k].second;

            int _step = abs(i - zero_i) + abs(j - zero_j);
            step = min(step, _step);
            if (step == 1) {
                return step;
            }
        }
        return step;
    }
};