
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        const unordered_set<string> word_set(wordDict.begin(), wordDict.end());
        vector<bool> flag (s.size() + 1, false);
        flag[0] = true;
        return _wordBreak(s, 0, word_set, flag);
    }
private:
    // DP method
    // 1. Recursive
    // 2. Memoize
    // 3. Bottom-up return
    bool _wordBreak(
        string s, 
        int idx,
        const unordered_set<string> & word_set,
        vector<bool>& flag
    ) {

        if (idx >= s.size()) return true;

        for (string word: word_set) {
            if (idx + word.size() > s.size()) continue;
            if (s.substr(idx, word.size()) == word) {
                flag[idx + word.size()] = true;
            }
        }

        if (flag[flag.size() - 1])  return true;

        // Find the next closest flag=1
        while (++idx < flag.size()) {
            if (flag[idx]) {
                return _wordBreak(s, idx, word_set, flag);
            }
        }
        return false;
    }
};