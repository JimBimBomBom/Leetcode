class Solution:
    def minimumLength(self, s: str) -> int:
        size = len(s)
        left = 0
        right = size - 1
        while left < right:
            if s[left] != s[right]:
                break
            while left < right and s[left] == s[left + 1]:
                left += 1
            while left < right and s[right] == s[right - 1]:
                right -= 1
            left += 1
            right -= 1
        
        return max(0, right - left + 1)
