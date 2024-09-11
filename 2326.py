class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1]*n for _ in range(m)]

        xOffset = 0
        yOffset = 0
        dir = "right"
        x = 0
        y = 0
        while head:
            el = head.val
            head = head.next

            result[y][x] = el
            if dir == "right":
                if x + 1 < n - xOffset:
                    x += 1
                else:
                    dir = "down"
                    y += 1
            elif dir == "down":
                if y + 1 < m - yOffset:
                    y += 1
                else:
                    dir = "left"
                    x -= 1
            elif dir == "left":
                if x - 1 >= xOffset:
                    x -= 1
                else:
                    dir = "up"
                    y -= 1
                    yOffset += 1
            elif dir == "up":
                if y - 1 >= yOffset:
                    y -= 1
                else:
                    dir = "right"
                    x += 1
                    xOffset += 1

        return result
        