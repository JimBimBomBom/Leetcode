class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        elements = [0 for _ in range(target + 1)]
        for c in candidates:
            if c <= target:
                elements[c] += 1
            
        def dfs(index, path, target, result, sum):
            if (sum + index) > target:
                return result

            if elements[index] == 0:
                return result
            if (target - sum) % index == 0 and (target - sum) // index <= elements[index]:
                # resPath = path + [index] * ((target - sum) // index)
                result.append(path + [index] * ((target - sum) // index))

            for i in range(min(target - sum // index, elements[index]), 0, -1):
                for j in range(index + 1, target + 1):
                    dfs(j, path + [index] * i, target, result, sum + i * index)
            return result


        result = list()
        for i in range(1, target + 1):
            result = dfs(i, [], target, result, 0)
        
        result = list(set([tuple(r) for r in result]))
        return result
        