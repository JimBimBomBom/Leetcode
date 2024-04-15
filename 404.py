class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        path = []
        path.append((root, False))

        result = 0
        while path:
            node = path.pop()

            if node[0].right:
                path.append((node[0].right, False))
            if node[0].left:
                path.append((node[0].left, True))

            if node[1] and not node[0].left and not node[0].right:
                result += node[0].val
        
        return result
