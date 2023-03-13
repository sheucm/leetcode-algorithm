class Solution {
public:
    string decodeString(string encoded_str) {

        if (encoded_str.size() == 1) return encoded_str;
        
        string ans;
        stack<string> s;
        for (int i = 0; i < encoded_str.size(); i++) {
            char c = encoded_str[i];

            if (is_letter(c)) {
                if (s.empty()) s.push({ c });
                else if (s.top() == "[") s.push({ c });
                else s.top().push_back(c);  // top is letters
            }
            else if (is_digit(c)) {
                if (s.empty()) 
                    s.push({ c });
                else {
                    if (is_digit(s.top()[0])) 
                        s.top().push_back(c);
                    else 
                        s.push({ c });
                }
            }
            else if (c == '[') {
                s.push({ c });
            }
            else if (c == ']') {
                string letters = s.top(); s.pop(); s.pop(); // 2nd pop is "["
                int k = stoi(s.top()); s.pop();
                
                string tmp;
                for (int j = 0; j < k; j++) tmp += letters; // repeat k times
                
                if (s.empty()) ans += tmp;
                else if (s.top() == "[") s.push(tmp);
                else s.top() += tmp;    // top is letters.
            }
            else {
                cout << "Warn: unexpected char=" << c << endl;
            }

        }

        while (!s.empty()) {
            ans += s.top(); s.pop();
        }
        return ans;
    }
private:
    bool is_letter(char c) {
        return c >= 'a' && c <= 'z';
    }
    bool is_digit(char c) {
        return c >= '0' && c <= '9';
    }
};