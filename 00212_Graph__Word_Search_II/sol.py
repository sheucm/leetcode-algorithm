class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ### Solution: Trie + DFS Backtracking
        ### Time Complexity: O(4^(M*N)*H)
        ### For X words search: Time Complexity: O(M*N*W*X)
        ### Can we do better?


        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
            curr.word = word
        

        ROWS, COLS = len(board), len(board[0])

        ans, path = set(), set()
        def dfs(r, c, parent):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in path or
                board[r][c] not in parent.children
            ):
                return
            
            char = board[r][c]
            node = parent.children[char]
            if node.is_word:
                ans.add(node.word)
            
            path.add((r, c))
            dfs(r+1, c, node)
            dfs(r, c+1, node)
            dfs(r-1, c, node)
            dfs(r, c-1, node)
            path.remove((r, c))  # Back tracking

            # Remove the word in Trie if it have been added to answer
            if not node.children:
                del parent.children[char]
            return
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)
        return list(ans)




