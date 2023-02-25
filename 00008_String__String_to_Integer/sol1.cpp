class Solution {
public:
    int myAtoi(string s) {
        
        
        char sign = '+';

        int idx = -1;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            if (c == ' ') {
                continue;
            }

            idx = i;
            break;
        }

        if (idx == -1) {
            return 0;
        }


        if (s[idx] == '+' || s[idx] == '-') {
            sign = s[idx++];
        }

        string num_str;
        for (int i = idx; i < s.size(); i++) {
            char c = s[i];
            if (is_num(c)) {
                num_str.push_back(c);
            } else {
                break;
            }
        }

        if (num_str.size() == 0) {
            return 0;
        }


        int num = _convert_to_num(num_str, sign);
        return num;
    }
private:
    const vector<char> nums {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    // 0: 48

    bool is_num(char c) {
        for (auto n : nums) {
            if (n == c) {
                return true;
            }
        }
        return false;
    }

    int _convert_to_num(string s, char sign) {
        double num = 0;
        int level = 0;
        int ret = 0;

        for (int i = s.size() - 1; i >= 0; i--) {
            char c = s[i];
            int n = c - 48;
            num += (c - 48) * pow(10, level);
            level++;

            if (num > INT_MAX) {
                ret = INT_MAX;
            }
        }

        if (ret == INT_MAX) {
            if (sign == '-') {
                ret = INT_MIN;
            }
        } else {
            ret = num * (sign == '+' ? 1 : -1);
        }

        return ret;
    }
};