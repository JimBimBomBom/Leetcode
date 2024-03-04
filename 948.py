class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        bestScore = 0
        currScore = 0

        while tokens:
            if power >= tokens[0]:
                power -= tokens.pop(0)
                currScore += 1
            elif currScore >= 1:
                power += tokens.pop()
                currScore -= 1
            else:
                break
            if currScore > bestScore:
                bestScore = currScore
        
        return bestScore
