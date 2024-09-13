class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        leftValueArr = [0 for _ in range(len(arr) + 1)]

        for i in range(1, len(arr) + 1):
            leftValueArr[i] = leftValueArr[i - 1] ^ arr[i - 1]

        for query in queries:
            left, right = query
            right += 1
            right = min(right, len(arr))
            result.append(leftValueArr[left] ^ leftValueArr[right])

        return result
        