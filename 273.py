class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"] 
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        indexes = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return "Zero"

        numStr = str(num)
        groups = []
        for i in range(len(numStr), 0, -3):
            groups.append(numStr[max(0, i - 3):i])

        result = ""
        groupIndex = 0
        for group in groups:
            size = len(group)
            one = int(group[size - 1])
            ten = int(group[size - 2]) if size >= 2 else 0
            oneIndex = int(group[size - 3]) if size >= 3 else 0
            if ten == 1:
                one += 10
                ten = 0
            
            if one or ten or oneIndex:
                result = indexes[groupIndex] + ' ' + result
            if one:
                result = ones[one] + ' ' + result  
            if ten:
                result = tens[ten] + ' ' + result
            if oneIndex:
                result = ones[oneIndex] + ' Hundred ' + result 
            groupIndex += 1

        result = result.strip()
        return result
