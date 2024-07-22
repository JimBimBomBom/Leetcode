class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def getLocalTree(node: TreeNode, to_delete: List[int], searchingForRoot: bool, result: List[TreeNode]):
            if searchingForRoot and node.val not in to_delete:
                result.append(node)
                searchingForRoot = False

            if node.left:
                if node.left.val in to_delete:
                    getLocalTree(node.left, to_delete, True, result)
                    node.left = None
                else:
                    getLocalTree(node.left, to_delete, searchingForRoot, result)

            if node.right:
                if node.right.val in to_delete:
                    getLocalTree(node.right, to_delete, True, result)
                    node.right = None
                else:
                    getLocalTree(node.right, to_delete, searchingForRoot, result)
        
        result = []
        getLocalTree(root, to_delete, True, result)

        return result
