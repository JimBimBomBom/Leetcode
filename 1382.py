# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            nonlocal nodes
            if not node:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def buildTree(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = buildTree(start, mid - 1)
            node.right = buildTree(mid + 1, end)
            return node

        return buildTree(0, len(nodes) - 1)
        