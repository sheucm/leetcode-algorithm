class Solution {
public:
    int characterReplacement(string s, int k) {
        if (k == s.size() || k == s.size() - 1) {
            return k;
        }

        set<char> _set;
        vector<int> letter_cnt (26, 0);
        for (int i = 0; i < s.size(); i++) {
            letter_cnt[s[i] - 'A']++;
            _set.insert(s[i]);
        }

        
        int max_len = 0;
        for (const char & target_c : _set) {
            
            if (letter_cnt[target_c - 'A'] + k <= max_len) {
                continue;
            }

            int window_left = -1;
            vector<int> changes;
            for (int i = 0; i < s.size(); i++) {

                if (s[i] == target_c) {
                    if (window_left == -1) {
                        window_left = i;
                    }
                }
                else if (k == 0) {
                    window_left = -1;
                    continue;
                }
                else {
                    changes.push_back(i);
                    if (changes.size() > k) {
                        int replace_idx = changes[0];
                        changes.erase(changes.begin());
                        window_left = replace_idx + 1;
                    }

                    if (window_left == -1) {
                        window_left = i;
                    }
                }
                
                max_len = max(max_len, i - window_left + 1);
            }
        }



        return max_len;
    }


};