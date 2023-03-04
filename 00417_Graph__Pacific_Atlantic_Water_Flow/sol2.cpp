#include <vector>
#include <iostream>
#include <queue>

using namespace std;
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        int M = heights.size();
        int N = heights[0].size();

        vector<vector<int>> pacific (M, vector<int>(N, 0));   // 0: not visit yet | 1: Pacific
        vector<vector<int>> atlantic (M, vector<int>(N, 0));   // 0: not visit yet | 1: Atlacnic

        // cal pacific side
        queue <vector<int>> q;
        for (int i = 0; i < M; i++) {
            q.push(vector<int>({i, 0}));
        }
        for (int j = 0; j < N; j++) {
            q.push(vector<int>({0, j}));
        }
        _bfs(q, pacific, heights, M, N);



        // cal atlantic
        q = queue <vector<int>>();
        for (int i = 0; i < M; i++) {
            q.push(vector<int>({i, N - 1}));
        }
        for (int j = 0; j < N; j++) {
            q.push(vector<int>({M - 1, j}));
        }
        _bfs(q, atlantic, heights, M, N);



        vector<vector<int>> ans;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (
                    pacific[i][j] == 1
                    && atlantic[i][j] == 1
                ) {
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
    
    void _bfs(
        queue <vector<int>>& q,
        vector<vector<int>>& flag,
        vector<vector<int>>& heights,
        int M, 
        int N
    ) {
        while (!q.empty()) {
            vector<int> cell = q.front();
            q.pop();

            int i = cell[0];
            int j = cell[1];

            flag[i][j] = 1;

            for (const vector<int>& dir : DIRS) {
                int _i = i + dir[0];
                int _j = j + dir[1];

                if (_i < 0 || _j < 0 || _i >= M || _j >= N) {
                    continue;
                }

                if (heights[_i][_j] >= heights[i][j] && flag[_i][_j] == 0) {
                    q.push(vector<int>({_i, _j}));
                }
            }
        }
    }
};

