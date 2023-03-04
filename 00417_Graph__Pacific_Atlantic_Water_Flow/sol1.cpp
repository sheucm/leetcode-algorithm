#include <vector>
#include <iostream>
#include <queue>

using namespace std;
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        const int M = heights.size();
        const int N = heights[0].size();

        vector<vector<bool>> is_confirmed (M, vector<bool>(N, false));
        vector<vector<bool>> is_dfs_visit (M, vector<bool>(N, false));
        vector<vector<int>> flows (M, vector<int>(N, NONE));

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                int flow = _dfs(i, j, M, N, is_confirmed, is_dfs_visit, flows, heights);
            }
        }

        vector<vector<int>> ans;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (flows[i][j] == BOTH) {
                    ans.push_back({i, j});
                }
            }
        }

        return ans;
    }


private:
    const vector<vector<int>> DIRS {
      {-1, 0},
      {0, -1},
      {1, 0},
      {0, 1}
    };
    const int NONE = 0;    // 0000
    const int PACIFIC = 1;  // 0001
    const int ATLANTIC = 2;     // 0010
    const int BOTH = 3;     // 0011

    int _dfs(
        int i,
        int j,
        const int M,
        const int N,
        vector<vector<bool>>& is_confirmed,
        vector<vector<bool>>& is_dfs_visit,
        vector<vector<int>>& flows,     // 0: none | 1: Pacific | 2: Atlantic | 3: Both
        vector<vector<int>>& heights
    ) {


        if (is_confirmed[i][j]) {
            return flows[i][j];
        }

        is_dfs_visit[i][j] = true;

        // get neighbors
        queue<vector<int>> q;
        q.push(vector<int>({i, j}));

        // expand neighbors if neighbors is same height.
        vector<vector<int>> same_height_cells;
        vector<vector<int>> neighbors;
        int& curr_flow = flows[i][j];

        while (!q.empty()) {
            vector<int> p = q.front();
            q.pop();

            for (auto & dir : DIRS) {
                int _i = p[0] + dir[0];
                int _j = p[1] + dir[1];

                if (_is_pacific(_i, _j)) {
                    curr_flow |= PACIFIC;
                }
                else if (_is_atlantic(_i, _j, M, N)) {

                    curr_flow |= ATLANTIC;
                }
                else if (heights[_i][_j] < heights[i][j]) {
                    if (!is_dfs_visit[_i][_j]) {
                        curr_flow |= _dfs(_i, _j, M, N, is_confirmed, is_dfs_visit, flows, heights);
                    }
                }
                else if (heights[_i][_j] == heights[i][j]) {
                    if (!is_dfs_visit[_i][_j]) {
                      is_dfs_visit[_i][_j] = true;
                      same_height_cells.push_back({_i, _j});
                      q.push(vector<int>({_i, _j}));
                    }
                }
            }
        }

        for (vector<int> & cell : same_height_cells) {
            int _i = cell[0];
            int _j = cell[1];

            flows[_i][_j] = curr_flow;
            is_confirmed[_i][_j] = true;
            is_dfs_visit[_i][_j] = false;
        }

        is_confirmed[i][j] = true;
        is_dfs_visit[i][j] = false;
        return curr_flow;
    }

    bool _is_pacific(int i, int j) {
        return i < 0 || j < 0;
    }
    bool _is_atlantic(int i, int j, const int M, const int N) {
        return i >= M || j >= N;
    }
};

