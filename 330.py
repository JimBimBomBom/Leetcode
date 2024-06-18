class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        
        sum = 1
        for num in sorted(nums):
            if num > sum:
                while num > sum:
                    if sum > n:
                        return result
                    result += 1
                    sum += sum 
            if sum > n:
                return result
            sum += num
        
        while sum <= n:
            result += 1
            sum += sum
        
        return result
