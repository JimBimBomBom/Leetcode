class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []

        rows_num = len(land)
        cols_num = len(land[0])

        row = land[0]
        for row_index in rows_num:
            start = True
            for i in range(cols_num):
                if row[i] == 1 and start:
                    start = False
                    result.append((i, row_index, i, row_index))
                elif row[i] == 0 and not start:
                    result[-1] = (result[-1][0], result[-1][1], i, result[-1][1] + (i - result[-1][0]))
                    start = True
            
            if not start:
                result[-1] = (result[-1][0], result[-1][1], cols_num - 1, result[-1][1] + (cols_num - 1 - result[-1][0]))
            
            if row_index > 0:
                row = row.intersection(land[row_index])



            




        