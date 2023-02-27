class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        vector<int> ans;
        int i = 0;
        int j = 0;

        // Margin
        int LEFT = 0;
        int RIGHT = matrix[0].size() - 1;
        int TOP = 0;
        int BOTTOM = matrix.size() - 1;

        /*
        0: j++
        1: i++
        2: j--
        3: i--
        */
        int dir = 0;
        while(RIGHT >= LEFT && BOTTOM >= TOP) {

            // cout << "push " << matrix[i][j] << endl;

            ans.push_back(matrix[i][j]);

            // Get next i, j
            while (RIGHT >= LEFT && BOTTOM >= TOP) {
                if (dir == 0) {
                    if (j + 1 <=  RIGHT) {
                        j++;
                        break;
                    } else {
                        TOP++;
                    }
                }
                else if (dir == 1) {
                    if (i + 1 <= BOTTOM) {
                        i++;
                        break;
                    }
                    else {
                        RIGHT--;
                    }
                }
                else if (dir == 2) {
                    if (j - 1 >= LEFT) {
                        j--;
                        break;
                    }
                    else {
                        BOTTOM--;
                    }
                }
                else {
                    if (i - 1 >= TOP) {
                        i--;
                        break;
                    }
                    else {
                        LEFT++;
                    }
                }
                dir = (dir + 1) % 4;
            }
        }

        return ans;
    }
};