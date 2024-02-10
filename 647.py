class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        result = size
        for i in range(size):
            for j in range(size - 1, i, -1):
                if s[i:j] == s[i:j:-1]:
                    result += 1
                    print("Found palindrome", s[i:j])
        return result
