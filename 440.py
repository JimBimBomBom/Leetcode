class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        digitsLen = len(str(n))
        print(digitsLen)
        digitRange = [10**i for i in range(digitsLen)]
        print(digitRange)

        for cycle in range(1, 10):
            print("Cycle: ", cycle, " with K: ", k)
            if k <= digitsLen:
                print("result within first ", digitsLen, "results")
                return digitRange[max(k - 1, 0)]*cycle
            k -= digitsLen
            result = cycle * digitRange[-1]
            print("Result comes : ", k, " steps after ", result)
            for i in range(digitsLen - 1, -1, -1):
                if k > digitRange[i]:
                    k -= digitRange[i]
                    result += digitRange[i]
                elif k == digitRange[i]:
                    k -= digitRange[i]
                    break
                else:
                    num = result + k
                    if num > n:
                        break
                    return num

        return digitRange[k - 1]*cycle + k
