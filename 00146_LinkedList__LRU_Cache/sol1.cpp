class Node {
public:
    int key;
    int val;
    Node* prev;
    Node* next;

    Node(int key, int val) {
        this->key = key;
        this->val = val;
        prev = NULL;
        next = NULL;
    }
};

class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        this->count = 0;
        this->head = NULL;
        this->tail = NULL;
    }
    
    int get(int key) {

        if (nodes_map.find(key) == nodes_map.end()) return -1;
        int ret_val = nodes_map[key]->val;
        _move_to_tail(nodes_map[key]);
        return ret_val;
    }
    
    void put(int key, int value) {

        if (nodes_map.find(key) != nodes_map.end()) {
            // update
            nodes_map[key]->val = value;
            _move_to_tail(nodes_map[key]);
        }
        else if (count < capacity) {
            // append
            _add_node(key, value);
        }
        else {
            // replace
            _remove_head();
            _add_node(key, value);
        }

    }
private:
    int capacity;
    int count;
    Node* head;
    Node* tail;
    unordered_map<int, Node*> nodes_map;

    // get
    void _move_to_tail(Node* node) {

        if (!tail) {
            tail = node;
            return;
        }
        if (node == tail) {
            return;
        }



        if (node == head) {
            head = head->next;
        }

        if (node->prev) {
            node->prev->next = node->next;
        }
        if (node->next) {
            node->next->prev = node->prev;
        }


        node->prev = tail;
        node->next = NULL;

        if (tail != NULL) {
            tail->next = node;
        }
        tail = node;
    }

    void _add_node(int key, int val) {

        count++;
        Node* node = new Node(key, val);
        nodes_map[key] = node;
        _move_to_tail(node);
        if (!head) {
            head = node;
        }
    }

    // update
    void _remove_head() {
        count--;
        nodes_map.erase(head->key);
        if (count == 0) {
            delete head;
            head = NULL;
            tail = NULL;
            return;
        }
        Node* new_head = head->next;
        if (new_head) new_head->prev = NULL;
        delete head;
        head = new_head;
    }

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */