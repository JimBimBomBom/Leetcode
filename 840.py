class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0

        width = len(grid[0])
        height = len(grid)
        x = 0
        y = 0

        while y < height - 2:
            while x < width - 2:
                print(x, y)
                print(grid[y][x], grid[y][x + 1], grid[y][x + 2])
                print(grid[y + 1][x], grid[y + 1][x + 1], grid[y + 1][x + 2])
                print(grid[y + 2][x], grid[y + 2][x + 1], grid[y + 2][x + 2])
                # no element can be greater than 9 or less than 1
                if (grid[y][x] > 9 or grid[y][x] < 1) or (grid[y + 1][x] > 9 or grid[y + 1][x] < 1) or (grid[y + 2][x] > 9 or grid[y + 2][x] < 1):
                    print("here")
                    x += 1
                    continue
                elif (grid[y][x + 1] > 9 or grid[y][x + 1] < 1) or (grid[y + 1][x + 1] > 9 or grid[y + 1][x + 1] < 1) or (grid[y + 2][x + 1] > 9 or grid[y + 2][x + 1] < 1):
                    print("there")
                    x += 2
                    continue
                elif (grid[y][x + 2] > 9 or grid[y][x + 2] < 1) or (grid[y + 1][x + 2] > 9 or grid[y + 1][x + 2] < 1) or (grid[y + 2][x + 2] > 9 or grid[y + 2][x + 2] < 1):
                    print("everywhere")
                    x += 3
                    continue

                print("all values are between 1 and 9")

                # distinct elements
                nums = set([grid[y][x], grid[y][x + 1], grid[y][x + 2], grid[y + 1][x], grid[y + 1][x + 1], grid[y + 1][x + 2], grid[y + 2][x], grid[y + 2][x + 1], grid[y + 2][x + 2]])
                if len(nums) != 9:
                    print("Not all values are unique")
                    x += 1
                    continue
                    
                # sum of rows
                if not ((grid[y][x] + grid[y][x + 1] + grid[y][x + 2]) == (grid[y + 1][x] + grid[y + 1][x + 1] + grid[y + 1][x + 2]) == (grid[y + 2][x] + grid[y + 2][x + 1] + grid[y + 2][x + 2])):
                    print("sum of rows not equal")
                    x += 1
                    continue
                    
                # sum of columns
                if not ((grid[y][x] + grid[y + 1][x] + grid[y + 2][x]) == (grid[y][x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1]) == (grid[y][x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2])):
                    print("sum of columns not equal")
                    x += 1
                    continue
            
                # sum of diagonals
                if not ((grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2]) == (grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x])):
                    print("sum of diagonals not equal")
                    x += 1
                    continue

                print("Found: ", x, y)
                result += 1
                x += 1
            x = 0
            y += 1
        
        return result
