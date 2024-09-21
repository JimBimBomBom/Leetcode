class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        operators = []

        num = 0
        for c in expression:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                nums.append(num)
                num = 0
                operators.append(c)
        nums.append(num)

        print(nums)
        print(operators)

        result = []

        def painter(nums, operators):
            n = len(nums)
            canvas = [0 for _ in range(n + 1)]
            canvas[0] = 1
            canvas[n] = -1


