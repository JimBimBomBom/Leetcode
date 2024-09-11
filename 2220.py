class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startBinary = [0 for _ in range(30)]
        for i in range(30):
            startBinary[i] = (start >> i) & 1

        goalBinary = [0 for _ in range(30)]
        for i in range(30):
            goalBinary[i] = (goal >> i) & 1

        return sum([startBinary[i] != goalBinary[i] for i in range(30)])
        