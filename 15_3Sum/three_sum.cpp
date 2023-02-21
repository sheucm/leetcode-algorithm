#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
		
        
		vector<vector<int>> results;
		
		set<vector<int>> s;
		
		
		for (int i = 0; i < nums.size(); i++) {
			
			if (nums[i] > 0) {
				break;
			}
		
			int j = i + 1;
			int k = nums.size() -1;
			
			while (j < k) {
				int sum = nums[i] + nums[j] + nums[k];
				
				if (sum == 0) {
					s.insert({nums[i], nums[j], nums[k]});
					j++;
					k--;
				}
				else if (sum > 0) {
					k--;
				}
				else {
					j++;
				}
			}
		}
		
		for (auto triplets : s) {
			results.push_back(triplets);
		}
		return results;
    }

};
