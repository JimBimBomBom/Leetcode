class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preffersOnes = students.count(1)
        preffersZeros = students.count(0)

        for sandwich in sandwiches:
            if sandwich == 0:
                if preffersZeros > 0:
                    preffersZeros -= 1
                else:
                    break
            else:
                if preffersOnes > 0:
                    preffersOnes -= 1
                else:
                    break
            
        return preffersOnes + preffersZeros
        