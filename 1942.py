class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        result = 1
        curr_state = [(bricks, ladders)]
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                new_state = []
                for state in curr_state:
                    if state[0] >= diff:
                        new_state.append((state[0] - diff, state[1]))
                    if state[1] > 0:
                        new_state.append((state[0], state[1] - 1))

                if new_state == []:
                    result = i - 1
                    break
                # new_state.sort(key=lambda x: x[1])
                sorted_tuples = sorted(new_state, key=lambda x: (x[1], -x[0]))
                curr_state = [next(group) for _, group in groupby(sorted_tuples, key=lambda x: x[1])]
                print(curr_state)
                curr_state = new_state
            result = i
        return result
        