class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        const int M = grid.size();
        const int N = grid[0].size();

        vector<pair<int, int>> rotten;
        vector<pair<int, int>> fresh;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 2) {
                    rotten.push_back(pair<int, int>(i, j));
                }
                else if (grid[i][j] == 1) {
                    fresh.push_back(pair<int, int>(i, j));
                }
            }
        }

        int t = -1;
        const vector<int> DIR {0, 1, 0, -1, 0};
        vector<pair<int, int>> next = rotten;

        do {
            t++;
            rotten = next;
            next.clear();
            for (int k = 0; k < rotten.size(); k++) {
                auto [i, j] = rotten[k];

                for (int d = 0; d < 4; d++) {
                    int _i = i + DIR[d];
                    int _j = j + DIR[d + 1];

                    if (_i < 0 || _i >= M || _j < 0 || _j >= N) {
                        continue;
                    }

                    if (grid[_i][_j] == 1) {
                        grid[_i][_j] = 2;
                        next.push_back(pair<int, int>(_i, _j));
                    }
                }
            }
        } while (next.size() > 0);



        for (auto p : fresh) {
            auto [i, j] = p;
            if (grid[i][j] == 1) {
                return -1;
            }
        }

        return t;
    }
};