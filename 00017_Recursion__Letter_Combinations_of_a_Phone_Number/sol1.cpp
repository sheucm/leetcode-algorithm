class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits == "") return {};
        init_m();
        vector<string> ans {""};
        for (int i = 0; i < digits.size(); i++) {
            ans = combination(ans, m[digits[i]]);
        }        
        return ans;
    }
private:
    unordered_map<char, vector<string>> m;
    void init_m () {
        m['2'] = vector<string> ({"a", "b", "c"});
        m['3'] = vector<string> ({"d", "e", "f"});
        m['4'] = vector<string> ({"g", "h", "i"});
        m['5'] = vector<string> ({"j", "k", "l"});
        m['6'] = vector<string> ({"m", "n", "o"});
        m['7'] = vector<string> ({"p", "q", "r", "s"});
        m['8'] = vector<string> ({"t", "u", "v"});
        m['9'] = vector<string> ({"w", "x", "y", "z"});
    }


    vector<string> combination(
        vector<string>& list1,
        vector<string>& list2
    ) {
        vector<string> ret;
        for (const string & str1 : list1) {
            for (const string & str2 : list2) {
                ret.push_back(str1 + str2);
            }
        }
        return ret;
    }
};