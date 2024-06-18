class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        max = int(c ** 0.5)

        for i in range(0, max):
            largest = max - i
            remaining = (c - largest**2) ** 0.5

            if remaining == int(remaining):
                if int(largest**2) + int(remaining**2) == c:
                    return True

        return False
