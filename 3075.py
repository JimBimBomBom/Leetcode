class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)

        result = 0

        for index, el in enumerate(happiness[:k]):
            result += el - index
        
        return result
