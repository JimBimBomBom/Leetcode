class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        result_arr = [0 for i in range(101)]
        for num in nums:
            result_arr[num] += 1

        result_arr.sort(reverse=True)
        max_value = result_arr[0]
        result = 0
        for i in range(100):
            if result_arr[i] == max_value:
                result += max_value
            else:
                break
        
        return result
        