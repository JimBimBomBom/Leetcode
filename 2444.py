class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lowerBoundIndexes = []
        upperBoundIndexes = []

        for index, num in enumerate(nums):
            if num == minK:
                lowerBoundIndexes.append(index)
            elif num == maxK:
                upperBoundIndexes.append(index)
        
        if minK == maxK:
            result = 0
            for i in range(1, len(lowerBoundIndexes) + 1):
                result += i
            return result
        else:
            return len(lowerBoundIndexes) * len(upperBoundIndexes)
        