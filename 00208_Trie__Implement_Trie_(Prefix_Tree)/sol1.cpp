class Node {
public:
    string val;
    unordered_map<char, Node*> edges;

    Node() {}
    Node(string val) {
        this->val = val;
    }
};
class Trie {
public:
    Trie() {
        root = new Node("*");
    }
    
    void insert(string word) {
        _insert(root, word, 0);
    }
    
    bool search(string word) {
        return _search(root, word, 0, false);
    }
    
    bool startsWith(string prefix) {
        return _search(root, prefix, 0, true);
    }

private:
    Node* root;

    void _insert(Node* _root, string& word, int i) {
        if (i == word.size()) {
            _root->val = word;
            return;
        }
        if (_root->edges.find(word[i]) == _root->edges.end()) {
            _root->edges[word[i]] = new Node();
        }
        Node* next = _root->edges[word[i]];
        _insert(next, word, i+1);
    }

    bool _search(Node* _root, string& word, int i, bool is_starts_with) {
        if (i == word.size()) {
            if (is_starts_with) return true;
            return _root->val == word;
        }
        if (_root->edges.find(word[i]) == _root->edges.end()) {
            return false;
        }
        Node* next = _root->edges[word[i]];
        return _search(next, word, i+1, is_starts_with);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */