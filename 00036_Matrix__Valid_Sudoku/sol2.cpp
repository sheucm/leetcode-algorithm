class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        

        // validate rows
        for (int row = 0; row < 9; row++) {
            vector<bool> seen (10, false);
            for (int col = 0; col < 9; col++) {    
                const char& c = board[row][col];
                if (c == '.') {
                    continue;
                }
                if (seen[c - '0']) {
                    return false;
                }
                seen[c - '0'] = true;
            }
        }

        // validate cols
        for (int col = 0; col < 9; col++) {
            vector<bool> seen (10, false);
            for (int row = 0; row < 9; row++) {
                const char& c = board[row][col];
                if (c == '.') {
                    continue;
                }
                if (seen[c - '0']) {
                    return false;
                }
                seen[c - '0'] = true;
            }
        }


        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                const int left = j;
                const int right = j + 2;
                const int top = i;
                const int bottom = i + 2;

                vector<bool> seen (10, false);
                for (int row = top; row <= bottom; row++) {
                    for (int col = left; col <= right; col++) {
                        const char& c = board[row][col];
                        if (c == '.') {
                            continue;
                        }
                        if (seen[c - '0']) {
                            return false;
                        }
                        seen[c - '0'] = true;
                    }
                }
            }
        }

        return true;
    }
};