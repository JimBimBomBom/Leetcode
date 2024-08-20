class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        leftArray = points[0]
        rightArray = points[0]
        centerArray = points[0]

        for i in range(1, len(points)):
            for j in range(1, len(points[0])):
                leftArray[j] = max(leftArray[j], leftArray[j - 1] - 1)
            for j in range(len(points[0]) - 2, -1, -1):
                rightArray[j] = max(rightArray[j], rightArray[j + 1] - 1)
            for j in range(len(points[0])):
                centerArray[j] += points[i][j]
            points[i] = [max(leftArray[j], rightArray[j], centerArray[j]) for j in range(len(points[0]))]
            print(points[i])
        
        return max(points[-1])
                