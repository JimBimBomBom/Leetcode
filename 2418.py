class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(names, heights))
        zipped.sort(key=lambda x: x[1], reverse=True)
        result, _ = list(zip(*zipped))
        return result
