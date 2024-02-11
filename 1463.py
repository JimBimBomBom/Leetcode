class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        colls = len(grid[0])
        robot1 = 0
        robot2 = colls - 1
        moves = [[[-1 for k in range(colls)] for j in range(colls)] for i in range(rows)]
        moves[0][robot1][robot2] = grid[0][robot1] + grid[0][robot2]

        for i in range(1, rows):
            for j1 in range(colls):
                for j2 in range(j1 + 1, colls):
                    best_value = -1

                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if (j1 + x >= 0 and j1 + x < colls and j2 + y >= 0 and j2 + y < colls):
                                curr_val = moves[i - 1][j1 + x][j2 + y]
                                if curr_val > best_value:
                                    best_value = curr_val
                    if best_value != -1:
                        moves[i][j1][j2] = best_value + grid[i][j1] + grid[i][j2]
        
        result = -1
        for j1 in range(rows):
            for j2 in range(j1 + 1, colls):
                curr_val = moves[rows - 1][j1][j2]
                if curr_val > result:
                    result = curr_val

        return result
            