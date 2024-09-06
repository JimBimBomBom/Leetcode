class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        currSum = sum(rolls)
        totalCount = m + n

        if (currSum + n*6) / totalCount == mean:
            return [6] * n
        
        for i in range(5, 0, -1):
            potentialSum = currSum + i * n
            if (potentialSum / totalCount) > mean:
                # print("hmm", i)
                continue
            for j in range(0, n + 1):
                # print("Test: ", f"i: {i}, j: {j}")
                if (potentialSum + j) / totalCount == mean:
                    # print(f"i: {i}, j: {j}")
                    return [i] * (n-j) + [i + 1] * j
        
        return []
        