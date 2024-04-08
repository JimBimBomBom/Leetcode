class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        size = len(s)

        s = list(s)
        while i < size - 1:
            if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
                s.pop(i)
                s.pop(i)
                size -= 2
                i = 0
                continue
            i += 1

        return "".join(str(word) for word in s)
        