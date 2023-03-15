
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {

        const unordered_set<string> word_set(wordDict.begin(), wordDict.end());
        
        vector<bool> flag (s.size() + 1, false);
        flag[0] = true;

        for (int i = 0; i < s.size(); i++) {
            if (!flag[i]) continue;
            for (string w: word_set) {
                if (s.substr(i, w.size()) == w) {
                    if (i + w.size() < flag.size()) {
                        flag[i + w.size()] = true;
                    }
                }
            }
        }

        return flag[s.size()];
    }
};