from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq.items(), key=lambda x: (x[1], -x[0]))

        result = []
        for num, count in freq:
            result.extend([num] * count)

        return result
        