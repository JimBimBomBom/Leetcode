# def findLargestDivisibleSubset(list: List[int]) -> List[int]:
#     best_result = []
#     for numI in list:
#         if len(list[list.index(numI):]) <= len(best_result):
#             break
#         curr_result = [numI]
#         for numJ in list[list.index(numI) + 1:]:
#             if numI % numJ == 0:
#                 curr_result.append(numJ)

#         if len(curr_result) <= len(best_result):
#             continue

#         curr_result.remove(numI)
#         curr_result = findLargestDivisibleSubset(curr_result)
#         curr_result.append(numI)

#         if len(curr_result) > len(best_result):
#             best_result = curr_result
#     return best_result

# def findLargestDivisibleSubset(nums: List[int]) -> List[int]:
#     best_result = []
#     for numI in nums:
#         curr_result = [numI] *2
#         while True:
#             i = nums.index(curr_result[-1]) + 1
#             curr_result.pop()
#             print("Curr result: ", curr_result)
#             if len(curr_result) < 1:
#                     break

#             while i < len(nums):
#                 numJ = nums[i]
#                 if curr_result[-1] % numJ == 0:
#                     print("Adding: ", numJ)
#                     curr_result.append(numJ)
#                     i = nums.index(numJ) + 1
#                 else:
#                     i += 1
#             if len(curr_result) > len(best_result):
#                 print("Old result: ", best_result, " < ", curr_result)
#                 best_result = curr_result.copy()

#     return best_result

def findLargestDivisibleSubset(nums: List[int]) -> List[int]: #works for sorted list
    best_result = 0
    group_size = [1] * len(nums)
    best_predecessor = [-1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if group_size[i] < group_size[j] + 1:
                    group_size[i] = group_size[j] + 1
                    best_predecessor[i] = j

        if group_size[i] > group_size[best_result]:
            best_result = i

    result = []
    while best_result != -1:
        result.append(nums[best_result])
        best_result = best_predecessor[best_result]

    return result

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        #print(nums)

        return findLargestDivisibleSubset(nums)

def main():
    s = Solution()
    print(s.largestDivisibleSubset([1,2,3]))
    print(s.largestDivisibleSubset([1,2,4,8]))
    print(s.largestDivisibleSubset([1,2,4,8,9,72]))