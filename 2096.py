class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findNodeWithPath(tree: TreeNode, value: int, path: str):
            if tree.val == value:
                return path
            if tree.left:
                result = findNodeWithPath(tree.left, value, path)
                if result != '-':
                    return result + 'L'
            if tree.right:
                result = findNodeWithPath(tree.right, value, path)
                if result != '-':
                    return result + 'R'
            return '-'
        
        pathStart = findNodeWithPath(root, startValue, '')
        pathDest = findNodeWithPath(root, destValue, '')

        pathStart = pathStart[::-1]
        pathDest = pathDest[::-1]
        # print(pathStart, pathDest)

        diff = min(len(pathStart), len(pathDest))
        for i in range(min(len(pathStart), len(pathDest))):
            if pathStart[i] != pathDest[i]:
                diff = i
                # print(diff)
                break
        
        result = 'U'*(len(pathStart) - diff) + pathDest[diff:]
        # print(result)

        return result
        