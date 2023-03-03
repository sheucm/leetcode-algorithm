class Node {
public:
    int val;
    vector<Node*> prerequisites;
    Node() {
        val = 0;
        prerequisites = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        prerequisites = vector<Node*>();
    }
    Node(int _val, vector<Node*> _children) {
        val = _val;
        prerequisites = _children;
    }
};
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        map<int, Node*> exists;

        for (int i = 0; i < prerequisites.size(); i++) {
            int course = prerequisites[i][0];
            int pre = prerequisites[i][1];
            Node* course_node = get_node(exists, course);
            Node* pre_node = get_node(exists, pre);
            course_node->prerequisites.push_back(pre_node);
        }

        // check if it's circular graph
        map<int, bool> is_visits;
        for (auto p : exists) {
            Node* start_node = p.second;
            if (is_visits.find(start_node->val) != is_visits.end()) {
                continue;
            }

            vector<int> path;
            bool _is_circular = is_circular(start_node, path, is_visits);
            if (_is_circular) {
                return false;
            }
        }

        return true;
    }
private:
    bool is_circular(
        Node* curr_node,
        vector<int>& path,
        map<int, bool>& is_visits
    ) {
        
        if (_find(path, curr_node)) {
            return true;
        }
        if (is_visits.find(curr_node->val) != is_visits.end()) {
            return false;
        }

        path.push_back(curr_node->val);
        is_visits[curr_node->val] = true;

        for (auto pre_node : curr_node->prerequisites) {
            bool _is_circular = is_circular(pre_node, path, is_visits);
            if (_is_circular) {
                return true;
            }
        }

        // step back
        path.pop_back();
        return false;
    }

    bool _find(vector<int>& paths, Node* node) {
        for (int i = 0; i < paths.size(); i++) {
            if (paths[i] == node->val) {
                return true;
            }
        }
        return false;
    }

    

    Node* get_node(map<int, Node*>& exists, int course) {
        Node* course_node = NULL;
        if (exists.find(course) == exists.end()) {
            course_node = new Node(course);
            exists[course] = course_node;
        }
        else {
            course_node = exists[course];
        }
        return course_node;
    }
};