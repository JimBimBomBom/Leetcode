class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        pos = (0, 0)
        subAreas = [pos]
        n = len(grid)
        firstSlash = True

        while True:
            c = grid[pos[0]][pos[1]]
            pos = (pos[0], pos[1] + 1)

            if c != " ":
                subAreas.append(pos)
                if firstSlash:
                    if c == "/":
                        pos = (pos[0] + 1, pos[1] - 1)
                        subAreas.append(pos)
                        firstSlash = False
                    else:
                        subAreas.append((pos[0] + 1, pos[1] + 1))
                        firstSlash = False



        