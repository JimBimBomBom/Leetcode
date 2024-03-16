class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        numberedPaths = {}
        sumVal = 0
        maxLen = 0
        for i, num in enumerate(nums):
            sumVal += 1 if num == 1 else -1
            if sumVal == 0:
                maxLen = i + 1
            elif sumVal in numberedPaths:
                maxLen = max(maxLen, i - numberedPaths[sumVal])
            else:
                numberedPaths[sumVal] = i
        return maxLen
