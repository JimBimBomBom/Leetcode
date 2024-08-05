class Solution:
    def minimumDeletions(self, s: str) -> int:
        aRemaining = sum([1 for c in s if c == 'a'])
        b = 0
        result = aRemaining
        for c in s:
            result = min(result, aRemaining + b)
            if c == 'a':
                aRemaining -= 1
            else:
                b += 1
            
        result = min(result, aRemaining + b)

        return result
