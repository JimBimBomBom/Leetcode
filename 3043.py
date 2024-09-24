class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1PrefixSet = set()
        arr1 = [str(el) for el in arr1]
        arr2 = [str(el) for el in arr2]
        for el in arr1:
            for i in range(1, len(el) + 1):
                arr1PrefixSet.add(el[:i])
        
        bestResult = 0
        arr2 = sorted(arr2, key=lambda x: len(x), reverse=True)
        for el in arr2:
            for i in range(len(el), 0, -1):
                if i < bestResult:
                    break
                if el[:i] in arr1PrefixSet:
                    if i > bestResult:
                        bestResult = i
        
        return bestResult
        