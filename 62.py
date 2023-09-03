import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array_2d = np.zeros((n, m))
        for y in range(0, m):
            for x in range(0, n):
                if y == 0:
                    array_2d[x][y] = 1
                elif x == 0:
                    array_2d[x][y] = 1
                else:
                    array_2d[x][y] = array_2d[x-1][y] + array_2d[x][y-1]
        result = int(array_2d[n-1][m-1])
        #print(array_2d)
        return result