class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def getLocalTree(node: TreeNode, distance: int) -> (int, [int]):
            if not node.left and not node.right:
                return 0, [1]
            
            total_count = 0
            leftDistances = []
            rightDistances = []
            if node.left:
                leftCount, leftDistances = getLocalTree(node.left, distance)
                total_count += leftCount
            if node.right:
                rightCount, rightDistances = getLocalTree(node.right, distance)
                total_count += rightCount

            for i in range(len(leftDistances)):
                for j in range(len(rightDistances)):
                    if leftDistances[i] + rightDistances[j] <= distance:
                        total_count += 1
            
            listDistances = [x+1 for x in leftDistances if x < distance]
            listDistances += [x+1 for x in rightDistances if x < distance]
            return total_count, listDistances

        result, _ = getLocalTree(root, distance)
        return result