class Solution {
public:
    vector<int> findAnagrams(string s, string p) {

        if (s.size() < p.size()) {
            return {};
        }

        vector<int> freq (26, 0);
        vector<int> window (26, 0);

        for (int i = 0; i < p.size(); i++) {
            freq[p[i] - 'a']++;
            window[s[i] - 'a']++;
        }

        vector<int> ans;
        if (window == freq) {
            ans.push_back(0);
        }

        for (int i = p.size(); i < s.size(); i++) {
            int last_idx = i - p.size();
            window[s[last_idx++] - 'a']--;
            window[s[i] - 'a']++;

            if (window == freq) {
                ans.push_back(last_idx);
            }
        }

        return ans;
    }


};