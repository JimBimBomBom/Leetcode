class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        result = 0
        size = len(piles)
        
        dp = [(0, 1, 0, True)] # actor == True means Alice
        while dp:
            index, m, intermediateResult, actor = dp.pop()

            for i in range(1, m * 2 + 1):
                if index + i > size:
                    result = max(result, intermediateResult + sum(piles[index:]))
                else:
                    dp.append((index + i, max(m, i), intermediateResult + sum(piles[index:max(index + i, size + 1)]), not actor))
        
        return result
            