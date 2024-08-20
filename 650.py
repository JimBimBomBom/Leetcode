class Solution:
    def minSteps(self, n: int) -> int:
        result = 0

        def largest_divisor(n: int) -> int:
            for i in range(n // 2, 1, -1):
                if n % i == 0:
                    return i
            return 1

        while n > 1:
            largestDivisor = largest_divisor(n)
            result += n // largestDivisor
            n = largestDivisor

        return result
        