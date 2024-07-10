class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        result = 0

        lastMealTime = 0

        for arrivalTime, cookTime in customers:
            if arrivalTime > lastMealTime:
                lastMealTime = arrivalTime

            lastMealTime += cookTime

            result += lastMealTime - arrivalTime

        return result / n
        