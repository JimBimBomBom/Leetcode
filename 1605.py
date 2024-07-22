class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)

        result = [[0 for _ in range(n)] for _ in range(m)]
        colIndex = 0
        colSum = zip(colSum, [i for i in range(n)])
        colSum = sorted(colSum, key=lambda x: x[0])
        for rowIndex in range(m):
            while rowSum[rowIndex] > 0 and colIndex < n:
                if rowSum[rowIndex] < colSum[colIndex][0]:
                    result[rowIndex][colSum[colIndex][1]] = rowSum[rowIndex]
                    colSum[colIndex] = (colSum[colIndex][0] - rowSum[rowIndex], colSum[colIndex][1])
                    rowSum[rowIndex] = 0
                elif rowSum[rowIndex] > colSum[colIndex][0]:
                    result[rowIndex][colSum[colIndex][1]] = colSum[colIndex][0]
                    rowSum[rowIndex] -= colSum[colIndex][0]
                    colIndex += 1
                else:
                    result[rowIndex][colSum[colIndex][1]] = rowSum[rowIndex]
                    rowSum[rowIndex] = 0
                    colIndex += 1

        return result
