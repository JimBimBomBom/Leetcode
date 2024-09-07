class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        potentialNodes = []
        first = head

        def dfs(node):
            if not node:
                return

            if node.val == first.val:
                potentialNodes.append(node)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        while head:
            newCandidates = []
            for node in potentialNodes:
                if head.val == node.val:
                    if not head.next:
                        return True
                    if node.left:
                        newCandidates.append(node.left)
                    if node.right:
                        newCandidates.append(node.right)

            if not newCandidates:
                return False
            potentialNodes = newCandidates
            
            head = head.next
        
        return False
        