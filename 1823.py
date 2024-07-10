class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = [i for i in range(1, n + 1)]
        popIndex = 0
        while True:
            if len(result) == 1:
                return result[0]
            # print(result)
            size = len(result)
            popIndex += (k - 1)
            popIndex %= size
            # print(result[popIndex])
            result.pop(popIndex)
