class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        const int m = matrix.size();    // rows
        const int n = matrix[0].size(); // cols
        vector<vector<bool>> is_visited (m, vector<bool>(n, false));
        vector<int> ans;
        int i = 0;
        int j = 0;

        /*
        0: j++
        1: i++
        2: j--
        3: i--
        */
        int dir = 0;
        bool no_next = false;
        while(!no_next) {

            cout << "push " << matrix[i][j] << endl;

            ans.push_back(matrix[i][j]);
            is_visited[i][j] = true;

            // Get next i, j
            int begin_dir = dir;
            
            while (true) {
                if (dir == 0) {
                    if (j + 1 < n && !is_visited[i][j + 1]) {
                        j++;
                        break;
                    }
                }
                else if (dir == 1) {
                    if (i + 1 < m && !is_visited[i + 1][j]) {
                        i++;
                        break;
                    }
                }
                else if (dir == 2) {
                    if (j - 1 >= 0 && !is_visited[i][j - 1]) {
                        j--;
                        break;
                    }
                }
                else {
                    if (i - 1 >= 0 && !is_visited[i - 1][j]) {
                        i--;
                        break;
                    }
                }
                dir = _next_dir(dir);
                if (dir == begin_dir) {
                    no_next = true;
                    break;
                }
            }
        }

        return ans;
    }

    int _next_dir(int dir) {
        return (dir + 1) % 4;
    }
};