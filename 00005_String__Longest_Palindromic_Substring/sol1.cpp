class Solution {
public:
    string longestPalindrome(string s) {


        string ans;
        for (int i = 0; i < s.size(); i++) {

            int l;
            int r;

            // case 1: ans length is even
            if (i > 0 && s[i] == s[i-1]) {
                l = i - 1;
                r = i;
                _run(s, ans, l, r);
            } 


            // case 2: ans length is odd
            l = i;
            r = i;
            _run(s, ans, l, r);
        }

        return ans;
    }

private:
    void _run(const string& s, string& ans, int l, int r) {
        while (r < s.size() && l >= 0) {
            if (s[l] == s[r]) {
                l--;
                r++;
            } else {
                break;
            }
        }
        int length = r - l - 1;
        if (length > ans.size()) {
            ans.clear();
            for (int j = l + 1; j < r; j++) {
                ans.push_back(s[j]);
            }
        }
    }
};