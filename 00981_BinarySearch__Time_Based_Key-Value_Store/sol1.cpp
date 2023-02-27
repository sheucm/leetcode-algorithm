class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if (ts_list.count(key)) {
            ts_list[key].push_back(timestamp);
        }
        else {
            ts_list[key] = vector<int>({ timestamp });
        }
        values[key + "_" + to_string(timestamp)] = value;
    }
    
    string get(string key, int timestamp) {
        if (!ts_list.count(key)) {
            return "";
        }
        int t = -1;
        for (int i = ts_list[key].size() - 1; i >= 0; i--) {
            if (ts_list[key][i] <= timestamp) {
                t = ts_list[key][i];
                break;
            }
        }
        if (t == -1) {
            return "";
        }
        return values[key + "_" + to_string(t)];
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