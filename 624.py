class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minEls = [(arrays[0][0], 0), (arrays[1][0], 1)]
        maxEls = [(arrays[0][-1], 0), (arrays[1][-1], 1)]

        minEls.sort(key=lambda x: x[0])
        maxEls.sort(key=lambda x: x[0])

        for i in range(2, len(arrays)):
            if arrays[i][0] < minEls[0][0]:
                minEls[1] = minEls[0]
                minEls[0] = (arrays[i][0], i)
            elif arrays[i][0] < minEls[1][0]:
                minEls[1] = (arrays[i][0], i)

            if arrays[i][-1] > maxEls[1][0]:
                maxEls[0] = maxEls[1]
                maxEls[1] = (arrays[i][-1], i)
            elif arrays[i][-1] > maxEls[0][0]:
                maxEls[0] = (arrays[i][-1], i)
        
        if minEls[0][1] != maxEls[1][1]:
            return maxEls[1][0] - minEls[0][0]
        else:
            return max(maxEls[0][0] - minEls[0][0], maxEls[1][0] - minEls[1][0])
