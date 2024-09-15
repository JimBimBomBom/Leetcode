class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = [False, False, False, False, False]
        posState = []

        for i in range(len(s)):
            posState.append(vowels.copy())

            if s[i] == 'a':
                vowels[0] = not vowels[0]
            elif s[i] == 'e':
                vowels[1] = not vowels[1]
            elif s[i] == 'i':
                vowels[2] = not vowels[2]
            elif s[i] == 'o':
                vowels[3] = not vowels[3]
            elif s[i] == 'u':
                vowels[4] = not vowels[4]
        
        maxResult = 0
        for x in range(0, len(s)):
            for y in range(len(s) - 1, x - 1, -1):
                if y - x + 1 <= maxResult:
                    break
                if x == y:
                    if maxResult < 1 and s[x] != 'a' and s[x] != 'e' and s[x] != 'i' and s[x] != 'o' and s[x] != 'u':
                        maxResult = 1
                else:
                    currState = posState[y].copy()
                    change = False
                    if s[y] == 'a':
                        currState[0] = not currState[0]
                        change = True
                    elif s[y] == 'e':
                        currState[1] = not currState[1]
                        change = True
                    elif s[y] == 'i':
                        currState[2] = not currState[2]
                        change = True
                    elif s[y] == 'o':
                        currState[3] = not currState[3]
                        change = True
                    elif s[y] == 'u':
                        currState[4] = not currState[4]
                        change = True
                    
                    if posState[x] == currState:
                        if y - x >= maxResult:
                            maxResult = (y - x + 1)
                            if change:
                                continue
                            if s[y] == 'a' or s[y] == 'e' or s[y] == 'i' or s[y] == 'o' or s[y] == 'u':
                                maxResult -= 1
        return maxResult
