class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = None

        stack = [root]

        def stack_to_str(stack):
            return ''.join([chr(97 + node.val) for node in stack])

        def dfs(node, smallest):
            if node.left:
                stack.append(node.left)
                smallest = dfs(node.left, smallest)
                stack.pop()
            if node.right:
                stack.append(node.right)
                smallest = dfs(node.right, smallest)
                stack.pop()

            if not node.left and not node.right:
                currString = stack_to_str(stack)[::-1]
                if not smallest:
                    smallest = currString
                elif smallest > currString:
                    smallest = currString
        
            return smallest
        
        return dfs(root, smallest)
        