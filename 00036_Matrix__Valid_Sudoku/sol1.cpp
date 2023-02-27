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

        // validate boxes
        // {left, right, top, bottom}
        vector<vector<int>> nine_boxes {
            {0, 2, 0, 2},
            {3, 5, 0, 2},
            {6, 8, 0, 2},
            {0, 2, 3, 5},
            {3, 5, 3, 5},
            {6, 8, 3, 5},
            {0, 2, 6, 8},
            {3, 5, 6, 8},
            {6, 8, 6, 8},
        };
        for (int i = 0; i < 9; i++) {
            const auto& box = nine_boxes[i];
            const int& left = box[0];
            const int& right = box[1];
            const int& top = box[2];
            const int& bottom = box[3];


                // validate cols
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

        return true;
    }
};