class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (string token : tokens) {
            if (token == "+") {
                int n1 = s.top(); s.pop();
                int n2 = s.top(); s.pop();
                s.push(n2 + n1);
            }
            else if (token == "-") {
                int n1 = s.top(); s.pop();
                int n2 = s.top(); s.pop();
                s.push(n2 - n1);
            }
            else if (token == "*") {
                int n1 = s.top(); s.pop();
                int n2 = s.top(); s.pop();
                s.push(n2 * n1);
            }
            else if (token == "/") {
                int n1 = s.top(); s.pop();
                int n2 = s.top(); s.pop();
                s.push(n2 / n1);
            }
            else {
                s.push(stoi(token));
            }
        }
        int ans = s.top(); s.pop();
        return ans;
    }
};