class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x*-1 for x in nums if x < 0] + [x for x in nums if x >= 0]
        nums.sort()
        nums = [x*x for x in nums]
        return nums

        