class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsFound = set()

        for num in nums:
            if num in numsFound:
                return num
            numsFound.add(num)
        