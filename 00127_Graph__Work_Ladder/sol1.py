

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # O(N)
        if beginWord not in wordList:
            wordList = [beginWord] + wordList
        
        _m = {}

        # O(N * Lw)
        for idx, w in enumerate(wordList):
            for i in range(len(w)):
                key = w[:i] + '*' + w[i+1:]
                _m[key] = _m.get(key, []) + [idx]
        
        
        WORD = 0
        LEVEL = 1
        q = [(beginWord, 1)]
        visited = []

        ## BFS: O(N * Lw)
        while q:
            p = q.pop(0)
            if p[WORD] == endWord:
                return p[LEVEL]
            if p[WORD] in visited:
                continue
            visited.append(p[WORD])
            s = set()
            for i in range(len(p[WORD])):
                key = p[WORD][:i] + '*' + p[WORD][i+1:]
                for _next in _m.get(key, []):
                    s.add((wordList[_next], p[LEVEL] + 1))
            q = q + list(s)
        
        return 0

