class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minNum = min(nums)
        minIndex = nums.index(minNum)
        nums[0], nums[minIndex] = nums[minIndex], nums[0]

        def binarySearch(nums, target, start, end):
            if start > end:
                return start

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(nums, target, mid + 1, end)
            else:
                return binarySearch(nums, target, start, mid - 1)

        test = [nums[0]]
        for i in range(1, len(nums)):
            insertIndex = binarySearch(test, nums[i], 0, i - 1)
            test.insert(insertIndex, nums[i])
        
        return test
        