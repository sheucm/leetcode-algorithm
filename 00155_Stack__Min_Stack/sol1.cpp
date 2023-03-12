class MinStack {
public:
    MinStack() {
        min_val = INT_MAX;
    }
    
    void push(int val) {
        if (val < min_val) min_val = val;
        list.push_back(val);
    }
    
    void pop() {
        list.erase(list.end() - 1);
        min_val = _findMin();
    }
    
    int top() {
        return list[list.size() - 1];
    }
    
    int getMin() {
        return min_val;
    }
private:
    int min_val;
    vector<int> list;

    int _findMin() {
        int _min = INT_MAX;
        for (int n : list) {
            if (n < _min) _min = n;
        }
        return _min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */