class Solution {
public:
    int leastInterval(vector<char>& tasks, int N) {
        
        
        vector<int> cnt (26, 0);
        priority_queue<vector<int>> pq; // [cnt, char]
        for (char& task : tasks) {
            cnt[task - 'A']++;
        }
        for (int i = 0; i < cnt.size(); i++) {
            if (cnt[i]) pq.push({cnt[i], i + 'A'});
        }


        vector<char> ans;
        while (!pq.empty()) {
            vector<vector<int>> tmp;

            int K = N + 1;
            while (K--) {
                if (pq.empty()) {
                    ans.push_back('*');
                    continue;
                }
                auto _pop = pq.top(); pq.pop();
                ans.push_back(_pop[1]);
                if (--_pop[0] > 0) tmp.push_back(_pop);
            }

            for (auto & x : tmp) pq.push(x);
        }
        
        // clear * in the end
        int idx = ans.size() - 1;
        for (; idx >= 0; idx--) {
            if (ans[idx] != '*') break;
        }
        int count = idx + 1;
        return count;
    }
};