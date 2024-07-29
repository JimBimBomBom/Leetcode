class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = []

        for num in nums:
            mappedNums.append(int(''.join(str(mapping[int(c)]) for c in str(num))))
        
        zippedNums = list(zip(nums, mappedNums))
        zippedNums.sort(key=lambda x: x[1])

        return [num for num, _ in zippedNums]
        