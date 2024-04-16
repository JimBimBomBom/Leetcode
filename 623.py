# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        currDepth = 2
        stack = [(currDepth, root)]
        while stack:
            element = stack.pop()
            currNode = element[1]
            currDepth = element[0]

            if currDepth == depth:
                currNode.left = TreeNode(val, currNode.left)
                currNode.right = TreeNode(val, None, currNode.right)
            elif currDepth < depth:
                if currNode.right:
                    stack.append((currDepth + 1, currNode.right))
                if currNode.left:
                    stack.append((currDepth + 1, currNode.left))
                
        return root


