class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def sumList(lst):
            multiplicator = 1
            result = 0
            for el in lst[::-1]:
                result += el * multiplicator
                multiplicator *= 10
            return result

        stack = []
        def dfs(node):
            if not node.left and not node.right:
                return sumList(stack + [node.val])

            result = 0
            if node.left:
                stack.append(node.val)
                result += dfs(node.left)
                stack.pop()
            if node.right:
                stack.append(node.val)
                result += dfs(node.right)
                stack.pop()
            
            return result
        
        return dfs(root)
