class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        const int M = grid.size();
        const int N = grid[0].size();

        int cnt = 0;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == '1') {
                    cnt++;
                    _expand(i, j, M, N, grid);
                }
            }
        }
        return cnt;
    }
private:
    void _expand(
        int x,
        int y,
        const int M,
        const int N,
        vector<vector<char>>& grid
    ) {
        
        grid[x][y] = '2';
        const vector<int> DIR {0, 1, 0, -1, 0};
        for (int k = 0; k < 4; k++) {
            int _x = x + DIR[k];
            int _y = y + DIR[k + 1];

            if (_x < 0 || _x >= M || _y < 0 || _y >= N) {
                continue;
            }

            if (grid[_x][_y] == '1') {
                _expand(_x, _y, M, N, grid);
            }
        }
    }
};