class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max = 0
        longestStringOfMaxElement = 1
        localStringOfMaxElement = 0

        for num in nums:
            if num > max:
                max = num
                localStringOfMaxElement = 1
                longestStringOfMaxElement = 1
                continue
            if num == max:
                localStringOfMaxElement += 1
            else:
                if localStringOfMaxElement > longestStringOfMaxElement:
                    longestStringOfMaxElement = localStringOfMaxElement
                localStringOfMaxElement = 0

        if localStringOfMaxElement > longestStringOfMaxElement:
            longestStringOfMaxElement = localStringOfMaxElement
        localStringOfMaxElement = 0
        
        return longestStringOfMaxElement
