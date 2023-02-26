class Solution {
public:
    int characterReplacement(string s, int k) {
        if (k == s.size() || k == s.size() - 1) {
            return k;
        }

        int max_len = 0;
        for (int i = 0; i < 26; i++) {
            char c = i + 'A';
            max_len = max(max_len, _run(s, k, c));
        }

        return max_len;
    }


private:
    int _run(const string & s, int k, char c) {

        int left = 0;
        int i = 0;

        int max_len = 0;
        while(i < s.size() && left < s.size()) {
            
            while(i < s.size()) {
                if (s[i] == c) {
                    i++;
                }
                else if (k > 0) {
                    i++;
                    k--;
                }
                else {
                    break;
                }
            }

            max_len = max(max_len, i - left);


            if (s[left] != c) {
                k++;
            }
            left++; 

        }
        return max_len;
    }

};