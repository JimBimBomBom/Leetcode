class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        maxNum = max(nums)
        maxStrLen = len(str(maxNum))
        nums = [str(num) for num in nums]
        nums = sorted(nums, reverse=True, key=lambda x: (x + x[-1] * (maxStrLen - len(x))) if len(x) < maxStrLen else x)
        
        result = ''
        while len(nums) > 1:
            if (nums[0] + nums[1]) < (nums[1] + nums[0]):
                result += nums.pop(1)
            else:
                result += nums.pop(0)
        
        result += nums[0]
        
        return str(int(result))
