class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        const int start = _get_start(nums.size(), k);

        auto nums2 = vector<int>(nums);

        for (int i = 0; i < nums.size(); i++) {
            int val_idx = (start + i) % nums.size();
            int val = nums2[val_idx];
            nums[i] = val;
        }

    }
private:
    int _get_start(int size, int k) {
        int start = -k;
        while(start < 0) {
            start += size;
        }
        return start;
    }
};