class Solution:
    def reverseParentheses(self, s: str) -> str:
        subStrings = ['']

        for c in s:
            if c == '(':
                subStrings.append('')
            elif c == ')':
                appendString = subStrings.pop()
                subStrings[-1] += appendString[::-1] # NOTE: append reversed string
            else:
                subStrings[-1] += c

        return subStrings[0]
        