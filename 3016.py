class Solution:
    def minimumPushes(self, word: str) -> int:
        result = 0
        charOccurences = [0 for _ in range(26)]
        for c in word:
            charOccurences[ord(c) - ord('a')] += 1
        
        charOccurences.sort(reverse=True)
        times = 0
        for i in range(26):
            if i % 8 == 0:
                times += 1
            result += charOccurences[i] * times
        
        return result
