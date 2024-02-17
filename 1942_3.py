class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if ladders > 0:
            useLaderThreshold = bricks // ladders
        else:
            useLaderThreshold = bricks

        result = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                if diff > useLaderThreshold and ladders > 0:
                    ladders -= 1
                elif bricks >= diff:
                    bricks -= diff
                elif ladders > 0:
                    ladders -= 1
                else:
                    break
            result = i
            
        return result