class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        vector< vector<string> > ans;
        vector< vector<int> > ana_list;


        for (int i = 0; i < strs.size(); i++) {
            string word = strs[i];


            vector<int> ana (26, 0);
            for (int j = 0; j < word.size(); j++) {
                char c = word[j];
                ana[(c - 'a')]++;
            }

            
            bool is_found = false;
            for (int j = 0; j < ana_list.size(); j++) {

                if (ans[j][0].size() != word.size()) {
                    continue;
                }

                if (ana_list[j] == ana) {
                    ans[j].push_back(word);
                    is_found = true;
                    break;
                }
            }
            if (!is_found) {
                ana_list.push_back(ana);
                ans.push_back({ word });
            }
        }

        return ans;

    }
};