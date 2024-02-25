class Solution:
    primes = []
    primeSetForNums = []
    def init(self, nums):
        Solution.primes = Solution.sieveOfEratosthenes(max(nums))
        Solution.primes.sort()
        Solution.primeSetForNums = [set() for _ in range(len(nums))]
        Solution.findRootElements(nums)

    def sieveOfEratosthenes(n):
        primes = [True] * (n + 1)

        p = 3
        while p**2 < n:
            if primes[p]:
                for i in range(p**2, n+1, p):
                    primes[i] = False
            p += 2

        result = [i for i in range(3, n+1, 2) if primes[i]]
        result.insert(0, 2)
        return result

    def findRootElements(nums):
        for i, num in enumerate(nums):
            for prime in Solution.primes:
                if num < prime:
                    break
                if num % prime == 0:
                    Solution.primeSetForNums[i].add(prime)
                    num = num // prime

    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        uniqeuNums = set(nums)
        nums = list(uniqeuNums)
        size = len(nums)
        if nums[0] == 1:
            return False
        if size == 1:
            return True

        Solution().init(nums)
        indiciesToCheck = [False for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                if indiciesToCheck[i] and indiciesToCheck[j]:
                    continue
                for prime in Solution.primeSetForNums[i]:
                    if prime in Solution.primeSetForNums[j]:
                        indiciesToCheck[i] = True
                        indiciesToCheck[j] = True
                        break
            if not indiciesToCheck[i]:
                return False
        return True

Solution().canTraverseAllPairs([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]) # True
