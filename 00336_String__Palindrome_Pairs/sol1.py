class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        output = []
        reverse = {}
        for idx, word in enumerate(words):
            reverse[word[::-1]] = idx
        
        for idx, word in enumerate(words):
            if word in reverse and idx != reverse[word]:
                output.append([idx, reverse[word]])
            
            if word != "" and "" in reverse and word == word[::-1]:
                output.append([idx, reverse[""]])
                output.append([reverse[""], idx])
            
            for i in range(len(word)):
                if word[:i] in reverse and word[i:] == word[:i-1:-1]:
                    output.append([idx, reverse[word[:i]]])
                if word[i:] in reverse and word[:i] == word[i-1::-1]:
                    output.append([reverse[word[i:]], idx])

        return output
