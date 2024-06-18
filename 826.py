class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        result = 0
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs, key=lambda x: x[1], reverse=True)

        worker = sorted(worker, reverse=True)

        worker_index = 0
        for i in range(0, len(jobs)):
            while worker_index < len(worker) and worker[worker_index] >= jobs[i][0]:
                result += jobs[i][1]
                worker_index += 1
        
        return result
        