class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ratingCompact = [(0, 0) for _ in range(len(rating))]
        for i in range(1, len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    ratingCompact[i] = (ratingCompact[i][0] + 1, ratingCompact[i][1])
                else:
                    ratingCompact[i] = (ratingCompact[i][0], ratingCompact[i][1] + 1)

        result = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                if rating[i] < rating[j]:
                    result += ratingCompact[j][0]
                else:
                    result += ratingCompact[j][1]
        
        return result
        