class Solution:


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        neib = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neib[pattern] = neib.get(pattern, [])
                neib[pattern].append(word)
        
        q = [beginWord]
        visit = set()
        visit.add(beginWord)
        step = 1

        while q:
            tmp_set = set()
            for word in q:
                if word == endWord:
                    return step

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neib_word in neib[pattern]:
                        if neib_word not in visit:
                            tmp_set.add(neib_word)
                            visit.add(neib_word)
                
            q = list(tmp_set)
            step += 1

        return 0



