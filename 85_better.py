class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        colSize = len(matrix[0])

        heights = [0] * colSize
        for row in matrix:
            for x in range(colSize):
                if row[x] == '1':
                    heights[x] += 1
                else:
                    heights[x] = 0
            
            maxHeight = max(heights)
            for h in range(maxHeight, 0, -1):
                foundArea = 0
                for x in range(colSize):
                    if heights[x] >= h:
                        foundArea += h
                    else:
                        if foundArea > maxArea:
                            maxArea = foundArea
                        foundArea = 0

                if foundArea > maxArea:
                    maxArea = foundArea
                
        return maxArea
