class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = {}
        for i in range(65, 91): # A-Z
            count = tasks.count(chr(i))
            if count > 0:
                taskCount[chr(i)] = count
        
        taskCount = taskCount.items()

        maxTaskCount = max(taskCount, key=lambda x: x[1])[1]
        return max((n + 1)*maxTaskCount - ((n + 1) - sum(1 for x in taskCount if x[1] == maxTaskCount)), len(tasks))
