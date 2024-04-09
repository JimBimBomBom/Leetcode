class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0

        valueOfK = tickets[k]
        currValue = 0

        numOfSkippedValues = 0
        if k < len(tickets):
            numOfSkippedValues = len([tickets[i] for i in range(k + 1, len(tickets)) if tickets[i] >= valueOfK])
        
        while True:
            MinValue = min(tickets)
            result += len(tickets)*MinValue
            tickets = [ticket - MinValue for ticket in tickets if ticket - MinValue > 0]

            currValue += MinValue

            if valueOfK == currValue:
                return result - numOfSkippedValues
