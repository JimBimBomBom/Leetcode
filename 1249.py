class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        s = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
            elif s[i] == ')':
                counter -= 1
            
            if counter < 0:
                s[i] = ''
                counter += 1

        if counter > 0:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == '(':
                    s[i] = ''
                    counter -= 1
                if counter == 0:
                    break
        
        return "".join(str(word) for word in s)
        