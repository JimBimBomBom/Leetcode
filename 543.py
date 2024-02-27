# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    max = 0
    def calcDiameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.calcDiameterOfBinaryTree(root.left)
        right = self.calcDiameterOfBinaryTree(root.right)
        # print(root.val, left, right, self.max)
        
        if left + right > self.max:
            self.max = left + right
        
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calcDiameterOfBinaryTree(root)
        
        return self.max
