class Solution:
    def dfs(self, board, i, j, word):
        # print("DFS: ", i, j, word)
        stack = [(i, j, 0)]
        wordSize = len(word)

        currPath = []
        currValues = []
        currMax = 0
        while stack:
            element = stack.pop()
            i = element[0]
            j = element[1]

            if element[2] > currMax:
                currMax = element[2]

            if element[2] < currMax:
                while currValues and currValues[-1] >= element[2]:
                    currPath.pop()
                    currValues.pop()
                currMax = element[2]

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[element[2]] or (i, j) in currPath:
                continue

            currPath.append((i, j))
            currValues.append(element[2])

            if element[2] == wordSize - 1:
                return True

            stack.append((i - 1, j, element[2] + 1))
            stack.append((i + 1, j, element[2] + 1))
            stack.append((i, j - 1, element[2] + 1))
            stack.append((i, j + 1, element[2] + 1))
        
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word):
                        return True
        
        return False
        