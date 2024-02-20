class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        for i in range(size):
            if nums[i] != i:
                return i
        return size
