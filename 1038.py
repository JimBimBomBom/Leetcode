class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumOfNodes = 0
        def dfs(node):
            nonlocal sumOfNodes
            if not node:
                return
            sumOfNodes += node.val
            dfs(node.right)
            dfs(node.left)
        dfs(root)

        def dfs2(node):
            nonlocal sumOfNodes
            if not node:
                return
            dfs2(node.left)
            previousVal = node.val
            node.val = sumOfNodes
            sumOfNodes -= previousVal
            dfs2(node.right)
        dfs2(root)

        return root