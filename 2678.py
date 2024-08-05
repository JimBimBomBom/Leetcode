class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for senior in details if senior[11:13] > '60')
        