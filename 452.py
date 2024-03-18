class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intersectingBaloons = []
        points.sort(key=lambda x: (x[0], x[1]))

        while points:
            point = points.pop(0)
            intersectingBaloonsIndex = len(intersectingBaloons)
            intersectingBaloons.append(point)
            toDelete = []

            for intersectingPoint in points:
                if intersectingPoint[0] > intersectingBaloons[intersectingBaloonsIndex][1] or intersectingPoint[1] < intersectingBaloons[intersectingBaloonsIndex][0]:
                    break
                else:
                    toDelete.append(intersectingPoint)
                    intersectingBaloons[intersectingBaloonsIndex][0] = max(intersectingPoint[0], intersectingBaloons[intersectingBaloonsIndex][0])
                    intersectingBaloons[intersectingBaloonsIndex][1] = min(intersectingPoint[1], intersectingBaloons[intersectingBaloonsIndex][1])

            for intersectingPoint in toDelete:
                points.remove(intersectingPoint)
            
        return len(intersectingBaloons)
