class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        // key: char
        // val: last idx of the char
        unordered_map<char, int> last_idx;

        int ans = 0;
        int left = 0;
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (last_idx.count(c)) {
                left = max(left, last_idx[c] + 1);
            }
            last_idx[c] = i;
            ans = max(ans, i - left + 1);
        }
        
        return ans;
    }
};