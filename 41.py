class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = filter(lambda x: x >= 0, nums)
        sortedNums = sorted(set(nums))
        size = len(sortedNums)

        currLowest = 0
        for i in range(size):
            if currLowest == sortedNums[i] or currLowest == sortedNums[i] - 1:
                currLowest = sortedNums[i]
                continue
            else:
                break
        
        return currLowest + 1
