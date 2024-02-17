def ClimbBuilding(resources, ladderUseHeight, pointsOfInterest):
    currPath = 0
    for point in pointsOfInterest:
        if point > ladderUseHeight:
            resources = (resources[0], resources[1] - 1)
            currPath += 1
        elif resources[0] >= point:
            resources = (resources[0] - point, resources[1])
            currPath += 1
        elif resources[1] > 0:
            resources = (resources[0], resources[1] - 1)
            currPath += 1
        else:
            break
    return currPath

def ClimbBuilding1(resources, ladderUseHeight, heights):
    currPath = 0
    for i in range(1, len(heights)):
        diff = heights[i] - heights[i - 1]
        if diff > 0:
            if diff >= ladderUseHeight and resources[1] > 0:
                resources = (resources[0], resources[1] - 1)
                currPath += 1
            elif resources[0] >= diff:
                resources = (resources[0] - diff, resources[1])
                currPath += 1
            elif resources[1] > 0:
                resources = (resources[0], resources[1] - 1)
                currPath += 1
            else:
                break
        else:
            currPath += 1
    return currPath

def ClimbBuilding2(bricks, ladders, heights):
        result = 0
        curr_state = [(bricks, ladders)]
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                new_state = []
                for state in curr_state:
                    if state[0] >= diff:
                        new_state.append((state[0] - diff, state[1]))
                    if state[1] > 0:
                        new_state.append((state[0], state[1] - 1))

                if new_state == []:
                    result = i - 1
                    break
                # new_state.sort(key=lambda x: x[1])
                sorted_tuples = sorted(new_state, key=lambda x: (x[1], -x[0]))
                print(sorted_tuples)
                curr_state = [next(group) for _, group in groupby(sorted_tuples, key=lambda x: x[1])]
                print(curr_state)
            result = i
        return result

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) < 100:
            return ClimbBuilding2(bricks, ladders, heights)

        pointsOfInterest = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                pointsOfInterest.append(diff)

        
        sortedPoints = sorted(pointsOfInterest)
        heightPercentile = len(sortedPoints) / 100
        resources = (bricks, ladders)

        ladderUseThreshold = int(heightPercentile * 50)
        searchPercentile = 20

        bestPath = 0
        change = 0
        while True:
            ladderUseThreshold1 = ladderUseThreshold + int(heightPercentile * searchPercentile)
            ladderUseHeight1  = sortedPoints[ladderUseThreshold1]
            currPath1 = ClimbBuilding1(resources, ladderUseHeight1, heights)
            print(currPath1, ladderUseHeight1)

            ladderUseThreshold2 = ladderUseThreshold - int(heightPercentile * searchPercentile)
            ladderUseHeight2  = sortedPoints[ladderUseThreshold2]
            currPath2 = ClimbBuilding1(resources, ladderUseHeight2, heights)
            print(currPath2, ladderUseHeight2)

            chosenPath = bestPath
            if currPath1 >= currPath2 and currPath1 > bestPath:
                chosenPath = currPath1
                ladderUseThreshold = ladderUseThreshold1
            elif currPath2 > currPath1 and currPath2 > bestPath:
                chosenPath = currPath2
                ladderUseThreshold = ladderUseThreshold2

            currChange = chosenPath - bestPath
            if currChange <= change:
                searchPercentile = searchPercentile / 1.2
            change = currChange
            bestPath = chosenPath
            if searchPercentile < 0.01:
                break
        return bestPath
