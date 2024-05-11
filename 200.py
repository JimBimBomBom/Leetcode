class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rows_num = len(grid)
        cols_num = len(grid[0])

        for row in grid:
            start = True
            intervals = []
            for i in range(rows_num):
                if row[i] == '1' and start:
                    intervals.append((i, i))
                    start = False
                elif row[i] == '0' and not start:
                    intervals[-1] = (intervals[-1][0], i)
                    start = True

            print(intervals)

            if not start:
                intervals[-1] = (intervals[-1][0], cols_num)

            for interval in intervals:
                islandContinues = False
                for el in row[interval[0]:interval[1]]:
                    if el:
                        islandContinues = True
                        break
                if not islandContinues:
                    result += 1
        
        return result
        