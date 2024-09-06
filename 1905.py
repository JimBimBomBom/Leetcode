class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        result = 0

        solvedTiles = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and not solvedTiles[i][j] and grid1[i][j] == 1:
                    isIsland = True
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if x < 0 or y < 0 or x >= n or y >= m or grid2[x][y] == 0 or solvedTiles[x][y]:
                            continue
                    
                        solvedTiles[x][y] = True
                        stack.append((x + 1, y))
                        stack.append((x - 1, y))
                        stack.append((x, y - 1))
                        stack.append((x, y + 1))

                        if grid1[x][y] == 0:
                            isIsland = False
                    
                    if isIsland:
                        print(i, j)
                        print(grid1[i])
                        print(grid2[i])
                        result += 1
                    
                    print(solvedTiles)
        
        return result
