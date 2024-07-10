class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        sideEmptyBottles = 0

        while numBottles:
            emptyBottles = numBottles + sideEmptyBottles
            numBottles = emptyBottles // numExchange
            sideEmptyBottles = emptyBottles % numExchange
            result += numBottles

        return result
        