class Solution:
    def findComplement(self, num: int) -> int:
        binaryDigits = []

        result = 0
        while num != 0:
            binaryDigits.append(not(num % 2))
            num //= 2

        mult = 1
        for i in range(len(binaryDigits)):
            result += binaryDigits[i] * mult
            mult *= 2
        
        return result
        