class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set()
        for c in allowed:
            allowedSet.add(c)
        
        result = len(words)
        for word in words:
            for c in word:
                if c not in allowedSet:
                    result -= 1
                    break
        
        return result
        