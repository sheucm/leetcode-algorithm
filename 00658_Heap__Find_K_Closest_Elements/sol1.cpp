class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        
        // Heap solution

        unordered_map<int, vector<int>> dis_arr_mp; // [dis] = arr
        priority_queue<int, vector<int>, greater<int>> pq; // dis

        for (int a : arr) {
            int dis = abs(a - x);
            if (dis_arr_mp.find(dis) == dis_arr_mp.end()) {
                dis_arr_mp[dis] = vector<int>({ a });
                pq.push(dis);
            }
            else
                dis_arr_mp[dis].push_back(a);
        }

        vector<int> ans;
        while (!pq.empty()) {
            int dis = pq.top(); pq.pop();
            
            int remain = k - ans.size();
            if (dis_arr_mp[dis].size() < remain) {
                ans.insert(ans.end(), dis_arr_mp[dis].begin(), dis_arr_mp[dis].end());
            }
            else if (dis_arr_mp[dis].size() >= remain) {
                sort(dis_arr_mp[dis].begin(), dis_arr_mp[dis].end());
                ans.insert(ans.end(), dis_arr_mp[dis].begin(), dis_arr_mp[dis].begin() + remain);
                break;
            }
        }

        sort(ans.begin(), ans.end());

        return ans;
    }
};