class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dictionary = {}

        for description in descriptions:
            if description[0] not in dictionary:
                dictionary[description[0]] = TreeNode(description[0])
            if description[2] == 1:
                dictionary[description[0]].left = TreeNode(description[1])
            else:
                dictionary[description[0]].right = TreeNode(description[1])

        rootCandidates = set()
        notRootCandidates = set()
        for d in descriptions:
            rootCandidates.add(d[0])
            notRootCandidates.add(d[1])
        
        root = list(rootCandidates.difference(notRootCandidates)).pop()

        tree = dictionary[root]
        result = tree

        def fillTree(tree: TreeNode):
            tree = dictionary[tree.val]
            if tree.left and tree.left.val in dictionary:
                tree.left = fillTree(tree.left)
            if tree.right and tree.right.val in dictionary:
                tree.right = fillTree(tree.right)
            
            return tree
            
        fillTree(tree)

        return result
