class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(v, idx):
            if idx == len(word): 
                return v.is_word
            
            c = word[idx]
            if c in v.children:
                return dfs(v.children[c], idx+1)

            if c == '.':
                for k in v.children:
                    if dfs(v.children[k], idx+1):
                        return True
            return False
        return dfs(self.root, 0)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)