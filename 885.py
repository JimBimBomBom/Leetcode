class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]

        left = cStart - 1
        right = cStart + 1
        up = rStart - 1
        down = rStart + 1
        pos = [rStart, cStart]

        while True:
            pos[1] += 1

            if pos[1] < cols:
                while pos[0] < min(rows, down) :
                    result.append(pos.copy())
                    pos[0] += 1
            else:
                pos[1] = cols - 1
                pos[0] = down

            if pos[0] < rows:
                while pos[1] > max(-1, left):
                    result.append(pos.copy())
                    pos[1] -= 1
            else:
                pos[0] = rows - 1
                pos[1] = left

            if pos[1] >= 0:
                while pos[0] > max(-1, up):
                    result.append(pos.copy())
                    pos[0] -= 1
            else:
                pos[1] = 0
                pos[0] = up
            
            if pos[0] >= 0:
                while pos[1] <= min(cols - 1, right):
                    result.append(pos.copy())
                    pos[1] += 1
                pos[1] -= 1
            else:
                pos[0] = 0
                pos[1] = right
            
            if len(result) >= rows * cols:
                break
                
            left -= 1
            right += 1
            up -= 1
            down += 1

        return result
