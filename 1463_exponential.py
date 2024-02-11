def evaluateGrid(grid: List[List[int]]) -> List[List[int]]:
    new_grid = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            new_grid[i][j] = grid[i][j]

    for i in range(len(new_grid) - 2, 0, -1):
        for j in range(len(new_grid[0])):
            if j == 0:
                maximum = max(new_grid[i+1][j], new_grid[i+1][j+1])
                new_grid[i][j] += maximum
            elif j == len(new_grid[0]) - 1:
                maximum = max(new_grid[i+1][j-1], new_grid[i+1][j])
                new_grid[i][j] += maximum
            else:
                maximum = max(new_grid[i+1][j-1], new_grid[i+1][j], new_grid[i+1][j+1])
                new_grid[i][j] += maximum
    return new_grid

def getBestMove(grid: List[int], j: int) -> int:
    if j == 0:
        return max(grid[j], grid[j+1])
    elif j == len(grid) - 1:
        return max(grid[j-1], grid[j])
    else:
        return max(grid[j-1], grid[j], grid[j+1])

def getSecondBestMove(grid: List[int], j: int) -> int:
    if j == 0:
        return min(grid[j], grid[j+1])
    elif j == len(grid) - 1:
        return min(grid[j-1], grid[j])
    else:
        return min(max(grid[j-1], grid[j]), max(grid[j], grid[j+1]), max(grid[j-1], grid[j+1]))

def getBestMoveIndex(grid: List[int], j: int) -> int:
    result = 0
    if j == 0:
        if grid[j] < grid[j+1]:
            result = j+1
        else:
            result = j
    elif j == len(grid) - 1:
        if grid[j-1] > grid[j]:
            result = j-1
        else:
            result = j
    else:
        if grid[j-1] > grid[j] and grid[j-1] >= grid[j+1]:
            result = j-1
        elif grid[j+1] > grid[j] and grid[j+1] > grid[j-1]:
            result = j+1
        else:
            result = j
    return result

def oldgetSecondBestMoveIndex(grid: List[int], j: int) -> int:
    if j == 0:
        if grid[j] < grid[j+1]:
            return j
        else:
            return j+1
    elif j == len(grid) - 1:
        if grid[j-1] < grid[j]:
            return j-1
        else:
            return j
    else:
        if (grid[j-1] <= grid[j] and grid[j-1] >= grid[j+1]) or (grid[j-1] >= grid[j] and grid[j-1] <= grid[j+1]):
            return j-1
        elif (grid[j] <= grid[j-1] and grid[j] >= grid[j+1]) or (grid[j] >= grid[j-1] and grid[j] <= grid[j+1]):
            return j
        else:
            return j+1

def getSecondBestMoveIndex(grid: List[int], j: int, best: int) -> int:
    if j == 0:
        if best == j:
            return j+1
        else:
            return j
    elif j == len(grid) - 1:
        if best == j:
            return j-1
        else:
            return j
    else:
        if best == j-1:
            if grid[j] < grid[j+1]:
                return j+1
            else:
                return j
        elif best == j+1:
            if grid[j] < grid[j-1]:
                return j-1
            else:
                return j
        else:
            if grid[j-1] < grid[j+1]:
                return j+1
            else:
                return j-1

def addCherries(grid: List[int], robot1: int, robot2: int) -> int:
    cherries = 0
    if robot1 == robot2:
        cherries += grid[robot1]
    else:
        cherries += grid[robot1]
        cherries += grid[robot2]
    # print("Cherries: ", cherries, "Robot1: ", robot1, "with: ", grid[robot1], "and ", "Robot2: ", robot2, "with: ", grid[robot2])
    return cherries

def robotTraverseGrid(grid: List[List[int]]) -> int:
    result = 0
    robot1 = 0
    robot2 = len(grid[0]) - 1
    result += addCherries(grid[0], robot1, robot2)
    new_grid = evaluateGrid(grid)
    size = len(grid)
    print(new_grid)

    for i in range(1, size):
        r1BestMoveIndex = getBestMoveIndex(new_grid[i], robot1)
        r2BestMoveIndex = getBestMoveIndex(new_grid[i], robot2)
        if r1BestMoveIndex == r2BestMoveIndex:
            print("Robot1: ", r1BestMoveIndex, "Robot2: ", r2BestMoveIndex)
            if getSecondBestMove(new_grid[i], robot1) > getSecondBestMove(new_grid[i], robot2):
                robot1 = getSecondBestMoveIndex(new_grid[i], robot1, r2BestMoveIndex)
                robot2 = r2BestMoveIndex
            else:
                robot1 = r1BestMoveIndex
                robot2 = getSecondBestMoveIndex(new_grid[i], robot2, r1BestMoveIndex)
        else:
            robot1 = r1BestMoveIndex
            robot2 = r2BestMoveIndex
            print("Best move index: ", "Robot1: ", robot1, "Robot2: ", robot2)
            print("Best move value: ", "Robot1: ", grid[i][robot1], "Robot2: ", grid[i][robot2])
            print("Best MOVE value: ", "Robot1: ", new_grid[i][robot1], "Robot2: ", new_grid[i][robot2])
        result += addCherries(grid[i], robot1, robot2)
    return result

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        cherries = robotTraverseGrid(grid)
        return cherries
        