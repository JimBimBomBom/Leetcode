class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = list()
        row = list()
        row.append(1)
        pascal.append(row)       
        for idx in range(0, numRows - 1):
            row = list()
            left_val = 0
            right_val = 0
            for num in pascal[idx]:
                left_val = right_val
                right_val = num
                row.append(left_val + right_val)
            row.append(right_val)
            pascal.append(row)

        return pascal