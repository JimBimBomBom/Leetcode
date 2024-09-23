class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        foundSubstrings = []
        wordIndex = 0
        for word in dictionary:
            while wordIndex != -1:
                wordIndex = s.find(word, wordIndex)
                if wordIndex == -1:
                    wordIndex = 0
                    break
                foundSubstrings.append((wordIndex, wordIndex + len(word) - 1))
                wordIndex += len(word)

        dp = [i + 1 for i in range(n)]
        for i in range(n):
            options = [opt for opt in foundSubstrings if i == opt[1]]
            bestResult = i
            if options != []:
                for opt in options:
                    localResult = dp[max(opt[0] - 1, 0)]
                    for x in range(opt[0], opt[1]):
                        localResult = min(localResult, dp[x] + (opt[1] - x))
                        
                    if opt[0] == 0:
                        localResult = 0
                    if localResult < bestResult:
                        bestResult = localResult
                dp[i] = bestResult
            else:
                if i != 0:
                    dp[i] = dp[i-1] + 1
                
        return dp[-1]
