class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        size = len(nums)
        result = 0
        anchor = 0
        for leftIndex in range(size):
            currNumFrequency = 0
            for rightIndex in range(leftIndex, size):
                if nums[rightIndex] == maxElement:
                    currNumFrequency += 1
                if currNumFrequency == k:
                    anchor = rightIndex
                    break
            break
        
        if anchor == 0 and k != 1:
            return 0
        else:
            result += size - anchor

        for leftIndex in range(0, size - k):
            print(leftIndex)
            if nums[leftIndex] == maxElement:
                anchorChanged = False
                for rightIndex in range(anchor+1, size):
                    if nums[rightIndex] == maxElement:
                        anchor = rightIndex
                        anchorChanged = True
                        break
                if not anchorChanged:
                    break
            result += size - anchor
            
        return result
