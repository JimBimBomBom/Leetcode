class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        infoForNums = {}

        for i in range(-30, 31):
            count = nums.count(i)
            if count > 0:
                infoForNums[i] = (count, 1)
        print(infoForNums)

        for k, v in infoForNums.items():
            print(k, v)
            numTimes = v[0]
            for k2 in infoForNums.keys():
                if k2 != k:
                    infoForNums[k2] = (infoForNums[k2][0], infoForNums[k2][1] * (k**v[0]))
                else:
                    infoForNums[k2] = (infoForNums[k2][0], infoForNums[k2][1] * (k**(v[0] - 1)))
                print(k, k2, infoForNums[k2])

        result = [infoForNums[num][1] for num in nums]

        return result
