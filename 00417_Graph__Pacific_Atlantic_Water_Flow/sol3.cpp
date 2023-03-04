#include <vector>

using namespace std;
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        M = heights.size();
        N = heights[0].size();

        vector<vector<bool>> pacific (M, vector<bool>(N, 0)); 
        vector<vector<bool>> atlantic (M, vector<bool>(N, 0)); 

        for (int i = 0; i < M; i++) {
            _dfs(i, 0, pacific, heights);
            _dfs(i, N-1, atlantic, heights);
        }
        for (int j = 0; j < N; j++) {
            _dfs(0, j, pacific, heights);
            _dfs(M-1, j, atlantic, heights);
        }

        vector<vector<int>> ans;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    ans.push_back({i, j});
                }
            }
        }

        return ans;
    }


private:
    int M, N;
    const vector<vector<int>> DIRS {
      {-1, 0},
      {0, -1},
      {1, 0},
      {0, 1}
    };
    
    void _dfs(
        int i,
        int j,
        vector<vector<bool>>& flag,
        vector<vector<int>>& heights
    ) {
        if (flag[i][j]) {
            return;
        }

        flag[i][j] = true;

        for (const vector<int>& dir : DIRS) {
            int _i = i + dir[0];
            int _j = j + dir[1];

            if (_i < 0 || _j < 0 || _i >= M || _j >= N) {
                continue;
            }

            if (heights[_i][_j] >= heights[i][j] && flag[_i][_j] == 0) {
                _dfs(_i, _j, flag, heights);
            }
        }
    }
};

