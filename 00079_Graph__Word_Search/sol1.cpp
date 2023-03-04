class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
        const int M = board.size();
        const int N = board[0].size();

        vector<pair<int, int>> start_points;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == word[0]) {
                    start_points.push_back(pair<int, int>({i, j}));
                }
            }
        }

        for (const auto & p : start_points) {
            auto [i, j] = p;
            if (_dfs(i, j, 0, word, M, N, board)) {
                return true;
            }
        }
        return false;
        
    }
private:
    const vector<int> DIR {0, 1, 0, -1, 0};
    bool _dfs (
        int i, 
        int j,
        int word_idx,
        const string & word,
        const int M,
        const int N,
        vector<vector<char>>& board
    ) {
        if (board[i][j] == '*') {
            return false;
        }

        if (board[i][j] != word[word_idx]) {
            return false;
        }

        if (word_idx == word.size() - 1) {
            return true;
        }

        char c = board[i][j];
        board[i][j] = '*';

        bool is_found = false;
        for (int k = 0; k < 4; k++) {
            int _i = i + DIR[k];
            int _j = j + DIR[k + 1];
            if (_i < 0 || _i >= M || _j < 0 || _j >= N) {
                continue;
            }
            is_found = is_found || _dfs(_i, _j, word_idx + 1, word, M, N, board);
        }

        board[i][j] = c;
        return is_found;
    }
};