class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        // <sorted word, anagrams>
        unordered_map<string, vector<string> > m;

        for (int i = 0; i < strs.size(); i++) {
            const string& word = strs[i];

            string sorted = strs[i];
            sort(sorted.begin(), sorted.end());

            if (m.count(sorted)) {
                m[sorted].push_back({ word });
            }
            else {
                m[sorted] = vector<string>({ word });
            }
        }

        vector<vector<string>> ans;
        for (const auto & p : m) {
            ans.push_back(p.second);
        }
        return ans;

    }
};