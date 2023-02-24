class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int l = 0;
        int r = height.size() - 1;
        int ans = 0;

        while (r > l) {

            int w = r - l;
            int h = min(height[l], height[r]);
            int a = w * h;

            if (a > ans) {
                ans = a;
            }

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }  
};
