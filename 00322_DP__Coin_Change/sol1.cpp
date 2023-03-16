class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (!amount) return 0;

        // Use DP method
        vector<int> cnt (amount + 1);
        for (int i = 0; i <= amount; i++) {
            if (i != 0 && !cnt[i]) continue;
            for (int c : coins) {
                if (c >= cnt.size() - i) continue;
                int curr_cnt = cnt[i] + 1;
                if (!cnt[i + c]) cnt[i + c] = curr_cnt;
                else
                    cnt[i + c] = min(cnt[i + c], curr_cnt);
            }
        }
        if (cnt[amount] == 0) return -1;
        return cnt[amount];
    }
};