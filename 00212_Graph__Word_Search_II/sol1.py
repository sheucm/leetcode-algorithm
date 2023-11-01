class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert_word(self, word: str):
        curr = self.root
        for ch in word:
            if not curr.children.get(ch):
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_word = True
        curr.word = word

class Solution:

    def dfs(
        self,
        board: List[List[str]], 
        node: Node,
        visit_map: List[List[str]],
        i: int,
        j: int,
        collection: dict
    ):
        if node.is_word:
            collection[node.word] = True

        VISITED = -1
        visit_map[i][j] = VISITED

        b_len_y = len(board)
        b_len_x = len(board[0])

        dirs = [1, 0, -1, 0, 1]
        for x in range(4):
            ii = i + dirs[x]
            jj = j + dirs[x+1]

            
            if (
                ii >= 0 and ii < b_len_y and 
                jj >=0 and jj < b_len_x and
                visit_map[ii][jj] != VISITED and
                node.children.get(board[ii][jj])
            ):
                self.dfs(
                    board, 
                    node.children.get(board[ii][jj]), 
                    visit_map, 
                    ii, 
                    jj,
                    collection
                )
                
        visit_map[i][j] = 0



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()

        for w in words:
            trie.insert_word(w)
        
        rows = len(board)
        cols = len(board[0])

        answer = {}

        for i in range(rows):
            for j in range(cols):
                ch = board[i][j]
                if trie.root.children.get(ch):
                    visit_map = [ [0]*cols for x in range(rows) ]
                    self.dfs(
                        board,
                        trie.root.children.get(ch),
                        visit_map,
                        i, 
                        j,
                        answer
                    )
        return list(answer.keys())

