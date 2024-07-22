class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0
        a = 0
        b = 0

        for c in s:
            if c == 'a':
                if y > x and b > 0:
                    result += y
                    b -= 1
                    continue
                a += 1
            elif c == 'b':
                if x > y and a > 0:
                    result += x
                    a -= 1
                    continue
                b += 1
            else:
                if x > y:
                    result += y * min(a, b)
                else:
                    result += x * min(a, b)
                a = 0
                b = 0
                
        if x > y:
            result += y * min(a, b)
        else:
            result += x * min(a, b)

        return result
                    