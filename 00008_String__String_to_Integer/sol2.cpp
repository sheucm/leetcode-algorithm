class Solution {
public:
    int myAtoi(string s) {
        
        int idx = 0; 

        while (s[idx] == ' ') {
            idx++;
        }

        int sign = 1;
        if (s[idx] == '+' || s[idx] == '-') {
            sign = s[idx] == '+' ? 1 : -1;
            idx++;
        }

        double num = 0;
        bool out_of_boundary = false;
        for (int i = idx; i < s.size(); i++) {

            if (!(s[i] >= '0' && s[i] <= '9')) {
                break;
            }

            int n = s[i] - '0';
            num = num * 10 + n;

            if (
                num * sign > INT_MAX
                || num * sign < INT_MIN
            ) {
                out_of_boundary = true;
                break;
            }
        }

        if (out_of_boundary) {
            return sign == 1 ? INT_MAX : INT_MIN;
        }

        return (int) (num * sign);
    }
};