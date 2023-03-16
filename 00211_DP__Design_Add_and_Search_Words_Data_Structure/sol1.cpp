class Node {
public:
    string val;
    unordered_map<char, Node*> edges;

    Node() {}
    Node(string val) {
        this->val = val;
    }
};
class WordDictionary {
public:
    WordDictionary() {
        root = new Node("*");
    }
    
    void addWord(string word) {
        Node* curr = root;
        for (char c : word) {
            if (curr->edges.find(c) == curr->edges.end()) {
                curr->edges[c] = new Node();
            }
            curr = curr->edges[c];
        }
        curr->val = word;
    }
    
    bool search(string word) {
        return _search(root, word, 0);
    }
private:
    Node* root;

    bool _search(Node* curr, string& word, int i) {

        if (i >= word.size()) {
            return curr->val == word;
        };
        
        char& c = word[i];
        if (c == '.') {
            for (auto & itr : curr->edges) {
                c = itr.first;
                if (_search(itr.second, word, i + 1)) {
                    return true;
                }
                c = '.';
            }
            return false;
        }
        else if (curr->edges.find(c) == curr->edges.end()) {
            return false;
        }
        else {
            return _search(curr->edges[c], word, i + 1);
        }
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */