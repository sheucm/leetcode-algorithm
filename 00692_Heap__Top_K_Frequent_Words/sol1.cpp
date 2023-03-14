class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt_mp; // [word] = cnt
        unordered_map<int, vector<string>> cnt_words_mp; // [cnt] = words
        priority_queue<int> pq;

        for (string w : words) {
            if (cnt_mp.find(w) == cnt_mp.end()) cnt_mp[w] = 1;
            else cnt_mp[w]++;
        }

        for (auto & itr : cnt_mp) {
            string word = itr.first;
            int cnt = itr.second;

            if (cnt_words_mp.find(cnt) == cnt_words_mp.end()) {
                cnt_words_mp[cnt] = vector<string>({ word });
                pq.push(cnt);
            }
            else 
                cnt_words_mp[cnt].push_back(word);
        }

        vector<string> ans;
        while (!pq.empty()) {
            int cnt = pq.top(); pq.pop();

            sort(cnt_words_mp[cnt].begin(), cnt_words_mp[cnt].end());

            ans.insert(ans.end(), cnt_words_mp[cnt].begin(), cnt_words_mp[cnt].end());

            if (ans.size() >= k) break;
        }



        if (ans.size() > k) {
            ans.erase(ans.begin() + k, ans.end());
        }

        return ans;
    }
};