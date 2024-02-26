# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = [p]
        qStack = [q]
        while pStack and qStack:
            p = pStack.pop()
            q = qStack.pop()
            if p.val == q.val and p.val != None:
                pStack.append(p.left)
                qStack.append(q.left)
                pStack.append(p.right)
                qStack.append(q.right)
            elif p.val == q.val and p.val == None:
                continue
            else:
                return False

        return True
