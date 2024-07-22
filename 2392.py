class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(k)] for _ in range(k)]

        rowRes = [(set(), set()) for _ in range(k)]
        for i in range(len(rowConditions)):
            left, right = rowConditions[i]
            if right in rowRes[left][0]: # UNSAT
                return result
            rowRes[left][1].add(right)
            
            if left in rowRes[right][1]: # UNSAT
                return result
            rowRes[right][0].add(left)

        colRes = [(set(), set()) for _ in range(k)]
        for i in range(len(colConditions)):
            up, down = colConditions[i]
            if down in colRes[up][0]: # UNSAT
                return result
            colRes[up][1].add(down)

            if up in colRes[down][1]: # UNSAT
                return result
            colRes[down][0].add(up)

        
    