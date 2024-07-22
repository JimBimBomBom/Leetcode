class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMin = [min(row) for row in matrix]
        colMax = [max(col) for col in zip(*matrix)]

        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == rowMin[i] == colMax[j]]
