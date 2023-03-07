class Solution {
public:
    vector<int> findOrder(int N, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> NEXT (N);
        vector<vector<int>> PRE (N);
        for (int i = 0; i < prerequisites.size(); i++) {
            NEXT[prerequisites[i][1]].push_back(prerequisites[i][0]);
            PRE[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        // get leaf nodes
        vector<int> leaves;
        for (int i = 0; i < N; i++) {
            if (NEXT[i].size() == 0) {
                leaves.push_back(i);
            }
        }

        vector<int> order;
        vector<bool> is_visit (N);
        _bfs(leaves, PRE, NEXT, is_visit, order, N);

        for (int i = 0; i < N; i++) {
            if (!is_visit[i]) {
                order.clear();
                return order;
            }
        }

        reverse(order.begin(), order.end());

        return order;
    }

    
private:
    void _bfs(
        vector<int>& leaves,
        vector<vector<int>>& PARENTS,
        vector<vector<int>>& CHILDREN,
        vector<bool>& is_in_order,
        vector<int>& order,
        int N
    ) {
        while (leaves.size() > 0) {

            vector<int> next_leaves;
            vector<bool> is_added_to_next (N);

            for (int i = 0; i < leaves.size(); i++) {

                int leaf = leaves[i];

                if (is_in_order[leaf]) {
                    order.clear();
                    return;
                }

                order.push_back(leaf);
                is_in_order[leaf] = true;
				
				for (int parent : PARENTS[leaf]) {
                    _remove_item_from_list(CHILDREN[parent], leaf); // remove child 
                    if (!is_added_to_next[parent] && is_leaf(parent, CHILDREN)) {
                        is_added_to_next[parent] = true;
                        next_leaves.push_back(parent);
                    }
                }
            }
            leaves = next_leaves;
        }
    }

    bool is_leaf(int course, vector<vector<int>>& CHILDREN) {
        if (CHILDREN[course].size() == 0) return true;
        return false;
    }

    void _remove_item_from_list(vector<int>& list, int item) {
        // int found_idx = -1;
        // for (int i = 0; i < list.size(); i++) {
        //     if (list[i] == item) {
        //         found_idx = i;
        //         break;
        //     }
        // }
        // if (found_idx == -1) return;
        // list.erase(list.begin() + found_idx);

        auto idx = find(list.begin(), list.end(), item);
        if (idx == list.end()) return;
        list.erase(idx);
    }
};