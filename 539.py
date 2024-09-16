class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(timePoint[:2]) * 60 + int(timePoint[3:]) for timePoint in timePoints]
        timePoints.sort()

        result = 60*24 - abs(timePoints[-1] - timePoints[0])
        for i in range(len(timePoints) - 1):
            closestDifference = min(timePoints[i + 1] - timePoints[i], 60*24 - (timePoints[i + 1] - timePoints[i]))

            if closestDifference < result:
                result = closestDifference

        return result
        