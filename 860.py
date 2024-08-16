class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billFreqs = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                billFreqs[0] += 1
            elif bill == 10:
                if billFreqs[0] > 0:
                    billFreqs[0] -= 1
                    billFreqs[1] += 1
                else:
                    return False
            else:
                if billFreqs[1] > 0 and billFreqs[0] > 0:
                    billFreqs[1] -= 1
                    billFreqs[0] -= 1
                    billFreqs[2] += 1
                elif billFreqs[0] >= 3:
                    billFreqs[0] -= 3
                    billFreqs[2] += 1
                else:
                    return False
        
        return True