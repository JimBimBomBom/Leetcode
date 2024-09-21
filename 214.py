class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        result = s
        bestResult = n - 1
        edge = n//2
        for i in range(edge, -1, -1):
            leftS = s[:i]
            rightS = s[i + 1:2*i + 1]
            if leftS[::-1] == rightS:
                currResult = n - 1 - (2*i)
                if currResult < bestResult:
                    bestResult = currResult
                    suffix = s[i + 1:]
                    result =  suffix[::-1] + s[i] + suffix
            if i + 1 <= edge and s[i] == s[i + 1]:
                leftS = s[:i]
                rightS = s[i + 2: 2*i + 2]
                if i == 0 or leftS[::-1] == rightS:
                    currResult = n - 2 - (2*i)
                    if currResult < bestResult:
                        bestResult = currResult
                        suffix = s[i + 2:]
                        result = suffix[::-1] + s[i]*2 + suffix
            if bestResult < n - 1:
                return result

        if result == s and bestResult == n-1:
            suffix = s[1:]
            result = suffix[::-1] + s[0] + suffix
        
        return result
            