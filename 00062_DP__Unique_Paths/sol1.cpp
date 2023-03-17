class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 && n == 1) return 1;
        vector<vector<int>> dp (m, vector<int>(n));
        return _run(m-1, n-1, dp);
    }
private:
    int _run(int i, int j, vector<vector<int>>& dp) {
        if (i == 0 || j == 0) return 1;
        if (dp[i][j]) return dp[i][j];
        return dp[i][j] = _run(i-1, j, dp) + _run(i, j-1, dp);
    }
};