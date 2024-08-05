class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        size = len(nums)
        result = size
        area = sum(1 for num in nums if num == 1)
        if area == 0 or area == size:
            return 0
        
        index = 0
        oneCount = 0
        for num in nums:
            if num == 1:
                oneCount += 1
            index += 1

            if index >= area:
                result = min(result, area - oneCount)
                if nums[index - area] == 1:
                    oneCount -= 1
        
        nums = nums[size - area:] + nums[:area]

        index = 0
        oneCount = 0
        for num in nums:
            if num == 1:
                oneCount += 1
            index += 1

            if index >= area:
                result = min(result, area - oneCount)
                if nums[index - area] == 1:
                    oneCount -= 1
        
        return result
        