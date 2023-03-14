class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        
      // binary search solution

      auto ret = _find_pivot(arr, x);
      int l = ret[0];
      int r = ret[1];
      cout << "l=" << l << ", r=" << r << endl;

      vector<int> ans;
      if (l == r) {
        ans.push_back(arr[l]);
        l--;
        r++;
      }
  
      while (ans.size() < k) {
          int l_dis = INT_MAX;
          int r_dis = INT_MAX;
          
          if (l >= 0) {
            l_dis = abs(arr[l] - x);
          }
          if (r < arr.size()) {
            r_dis = abs(arr[r] - x);
          }
          
          if (l_dis == INT_MAX && r_dis == INT_MAX) break;
          
          if (l_dis <= r_dis) {
            ans.push_back(arr[l--]);
          }
          else {
            ans.push_back(arr[r++]);
          }
      }
      sort(ans.begin(), ans.end());
		  return ans;
		
    }
private:
    vector<int> _find_pivot(vector<int> & arr, int x) {

        int l = 0;
        int r = arr.size() - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (arr[m] == x) {
                l = r = m;
                break;
            }
            else if (arr[m] < x) {
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        if (r < 0) {
            l = r = 0;
        }
        else if (r < l) {
            int tmp = r;
            r = l;
            l = tmp;
        }
        return {l, r};
    }
};