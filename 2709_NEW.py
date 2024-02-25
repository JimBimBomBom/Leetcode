def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        uniqeuNums = set(nums)
        nums = list(uniqeuNums)
        size = len(nums)
        if size == 1 and nums[0] != 1:
            return True
        elif size == 1 and nums[0] == 1:
            return False

        indiciesToCheck = [False for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                if indiciesToCheck[i] and indiciesToCheck[j]:
                    continue
                if gcd(nums[i], nums[j]) != 1:
                    indiciesToCheck[i] = True
                    indiciesToCheck[j] = True
        return True

Solution().canTraverseAllPairs([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]) # True