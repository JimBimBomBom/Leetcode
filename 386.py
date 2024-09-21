class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        n = [str(i) for i in range(1, n + 1)]
        result = sorted(n, key=lambda x: tuple(x[i] for i in range(len(x))))
        result = [int(result[i]) for i in range(len(result))]

        return result
        