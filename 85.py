class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        rowSize = len(matrix)
        colSize = len(matrix[0])

        for y in range(rowSize):
            for x in range(colSize):
                if matrix[y][x] == '0':
                    continue

                searchInfo = (x, y, colSize)
                for down in range(y, rowSize):
                    if matrix[down][x] == '0':
                        break

                    right = searchInfo[2]
                    try:
                        right = matrix[down].index('0', searchInfo[0], searchInfo[2])
                    except ValueError:
                        pass

                    searchInfo = (searchInfo[0], searchInfo[1], right)

                    foundArea = (searchInfo[2] - searchInfo[0]) * (down - searchInfo[1] + 1)
                    if foundArea > maxArea:
                        maxArea = foundArea
        
        return maxArea
        