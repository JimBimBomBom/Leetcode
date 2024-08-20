class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        while True:
            n -= 1
            x = arr.pop(0)
            if n == 0:
                return x
            arr.append(x * 2)
            arr.append(x * 3)
            arr.append(x * 5)
            arr.sort()
            while arr[0] == x:
                arr.pop(0)
            