class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        
        for log in logs:
            if log == "../":
                result = max(0, result - 1)
            elif log != "./":
                result += 1
        
        return result
