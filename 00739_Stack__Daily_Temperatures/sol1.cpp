class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {

        if (T.size() == 1)  return { 0 };
        
        vector<int> ans (T.size(), 0);
        stack<int> s; // index stack
        for (int i = 0; i < T.size(); i++) {
            while (s.size() > 0) {
                if (T[i] <= T[s.top()]) break;
                int t = s.top(); s.pop();
                ans[t] = i - t;
            }
            s.push(i);
        }
        return ans;
    }

};