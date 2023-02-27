class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        ts_list[key].push_back(timestamp);
        values[key + "_" + to_string(timestamp)] = value;
    }
    
    string get(string key, int timestamp) {
        if (!ts_list.count(key)) {
            return "";
        }
        const auto & t_list = ts_list[key];
        int t = -1;
        int s = 0;
        int e = t_list.size() - 1;
        int m = 0;

        if (timestamp < t_list[0]) {
            return "";
        }

        while (s <= e) {
            m = (s + e) / 2;
            if (t_list[m] == timestamp) {
                e = m;
                break;
            }
            if (timestamp > t_list[m]) {
                // timestamp is between m ~ e
                s = m + 1;
            }
            else {
                // timestamp is between s ~ m
                e = m - 1;
            }
        }
        t = e;
        return values[key + "_" + to_string(t_list[t])];
    }

private:
    // <key, timestamps>
    unordered_map<string, vector<int>> ts_list;

    // <key_timestamp, value>
    unordered_map<string, string> values;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */