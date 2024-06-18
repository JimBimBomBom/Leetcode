class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0
        sorted_nums = sorted(nums)

        duplicate_nums_count = 0
        unique_nums = set(sorted_nums[0:1])

        for index in range(1, len(sorted_nums)):
            if sorted_nums[index] not in unique_nums:
                unique_nums.add(sorted_nums[index])
            else:
                duplicate_nums_count += 1

            if sorted_nums[index] > sorted_nums[index - 1]:
                diff = sorted_nums[index] - sorted_nums[index - 1] - 1

                result += duplicate_nums_count

                for _ in range(diff):
                    if duplicate_nums_count == 0:
                        break

                    duplicate_nums_count -= 1
                    result += duplicate_nums_count
            
        for i in range(0, duplicate_nums_count):
            result += duplicate_nums_count - i

        return result
        