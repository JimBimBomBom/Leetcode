class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # startIndex = 0
        # startSubIndex = left
        # endIndex = 0
        # endSubIndex = right
        # for steps in range(n, 0, -1):
        #     if startSubIndex > steps:
        #         startSubIndex -= steps
        #         startIndex += 1
        #     if endSubIndex > steps:
        #         endSubIndex -= steps
        #         endIndex += 1
        # print("index: ", startIndex)
        # print("subIndex: ", startSubIndex)
        # print("endIndex: ", endIndex)
        # print("endSubIndex: ", endSubIndex)

        # sums = []
        # for index in range(startIndex, endIndex):
        #     for subIndex in range(startSubIndex, n):
        #         print("Loop")
        #         print("index: ", index)
        #         print("subIndex: ", subIndex)
        #         sums.append(sum(nums[index:subIndex + 1]))
        # for subIndex in range(0, endSubIndex):
        #     print("Loop")
        #     print("index: ", endIndex)
        #     print("subIndex: ", subIndex)
        #     sums.append(sum(nums[endIndex:subIndex + 1]))
        # print(sums)
        result = [sum(nums[index:subIndex + 1]) for index in range(n) for subIndex in range(index, n)]
        return sum(sorted(result)[left - 1:right]) % (10 ** 9 + 7)
