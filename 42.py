class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        heightMap = [(i, height[i]) for i in range(len(height)) if height[i] > 0]
        heightMap.sort(key=lambda x: x[1], reverse=True)

        if len(heightMap) < 2:
            return 0

        maxHeight = heightMap.pop(0)[0]
        heightsBeingSolved = (maxHeight, maxHeight)
        resultForLayer = 0
        while True:
            if heightMap:
                currHeight = heightMap[0][1]
            else:
                break

            while heightMap and heightMap[0][1] == currHeight:
                newHeight = heightMap.pop(0)[0]
                if newHeight < heightsBeingSolved[0]:
                    resultForLayer += heightsBeingSolved[0] - newHeight - 1
                    heightsBeingSolved = (newHeight, heightsBeingSolved[1])
                elif newHeight > heightsBeingSolved[-1]:
                    resultForLayer += newHeight - heightsBeingSolved[-1] - 1
                    heightsBeingSolved = (heightsBeingSolved[0], newHeight)
                else:
                    resultForLayer -= 1
            
            layerCount = currHeight
            if heightMap:
                layerCount = currHeight - heightMap[0][1]

            result += layerCount * resultForLayer

        return result
