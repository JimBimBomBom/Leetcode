class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(sep=' ')
        words2 = s2.split(sep=' ')

        wordDict = dict()
        for word in words1:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        for word in words2:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        
        return [res for res in wordDict if wordDict[res] == 1]
        