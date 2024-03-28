class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        elementsInSubarray = dict()
        size = len(nums)
        leftIndex = 0
        rightIndexForCheck = 0
        maxSubarrayLength = 0

        for rightIndex in range(size):
            rightIndexForCheck = rightIndex

            elementsInSubarray[nums[rightIndex]] = elementsInSubarray.get(nums[rightIndex], 0) + 1
            if elementsInSubarray[nums[rightIndex]] > k:
                if rightIndex - leftIndex > maxSubarrayLength:
                    maxSubarrayLength = rightIndex - leftIndex

                while leftIndex <= rightIndex and elementsInSubarray[nums[rightIndex]] > k:
                    elementsInSubarray[nums[leftIndex]] -= 1
                    leftIndex += 1
        
        if (rightIndexForCheck - leftIndex) + 1 > maxSubarrayLength:
            maxSubarrayLength = (rightIndexForCheck - leftIndex) + 1
        
        return maxSubarrayLength
        