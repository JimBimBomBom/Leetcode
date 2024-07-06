class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = n - 1
        revolutions = time // cycle
        move = time % cycle

        if revolutions % 2 == 0:
            return move + 1
        else:
            return n - move
        