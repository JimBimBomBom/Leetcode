index = 0
jump_size = 0
curr_solution = ""
rightward_shift = 0


def move_back(jump_sizes, jump_indices):
    global index, jump_size, curr_solution, rightward_shift
    dot_index = curr_solution.rfind('.')
    curr_solution = curr_solution[:dot_index]
    jump_size = jump_sizes.pop()
    index = jump_indices.pop()


def move_forward(jump_sizes, jump_indices, string):
    global index, jump_size, curr_solution, rightward_shift
    curr_solution += string
    jump_sizes.append(jump_size)
    jump_indices.append(index)
    index += 1 + rightward_shift


def get_previous_jump(jump_sizes) -> int:
    return jump_sizes.pop()


def set_last_jump(jump_sizes, jump):
    jump_sizes.append(jump)


def within_range(min, max, value) -> bool:
    if value >= min and value <= max:
        return True
    return False


class Solution:
    def exit(self, message):
        print(message)
        exit()

    def canCross(self, stones: List[int]) -> bool:
        global index, jump_size, curr_solution, rightward_shift
        partial_results = dict()
        stone_pairs = dict()
        jump_sizes = []
        jump_indices = []

        if stones[1] - stones[0] != 1:
            return False
            # self.exit("1. First jump condition was not satisfied.")
        if len(stones) <= 2:
            return True

        jump_size = 1
        curr_solution = str(stones[0]) + '.' + str(stones[1])
        stone_count = len(stones)
        index = 2
        rightward_shift = 0
        while (index > 1 and index + rightward_shift < stone_count):
            rightward_shift = 0
            problem = False
            while partial_results.get(curr_solution + '.' + str(stones[index + rightward_shift])) == False:
                rightward_shift += 1
                if index + rightward_shift >= stone_count:
                    partial_results[curr_solution] = False
                    problem = True
                    break
                if rightward_shift > 2:
                    partial_results[curr_solution] = False
                    problem = True
                    break
            if problem:
                if not jump_indices or not jump_sizes:
                    return False

                keys_to_delete = [key for key in partial_results if key.startswith(
                    curr_solution) and key != curr_solution]
                for key in keys_to_delete:
                    del partial_results[key]
                move_back(jump_sizes, jump_indices)
                continue

            starting_point = stones[index - 1]
            jump_to_point = stones[index + rightward_shift]
            curr_distance = jump_to_point - starting_point

            curr_jump = str(stones[index - 1]) + '.' + \
                str(stones[index + rightward_shift])
            if stone_pairs.get((curr_jump, jump_size - 1)) or stone_pairs.get((curr_jump, jump_size)) or stone_pairs.get((curr_jump, jump_size + 1)):
                string = '.' + str(stones[index + rightward_shift])
                move_forward(jump_sizes, jump_indices, string)
                jump_size = curr_distance
                rightward_shift = 0
                continue

            if not within_range(jump_size - 1, jump_size + 1, curr_distance):
                partial_results[curr_solution + '.' +
                                str(stones[index + rightward_shift])] = False
                rightward_shift = 0
                continue
            else:
                string = '.' + str(stones[index + rightward_shift])

                move_forward(jump_sizes, jump_indices, string)
                jump_size = curr_distance
                stone_pairs[(curr_jump, jump_size - 1)] = True
                stone_pairs[(curr_jump, jump_size)] = True
                stone_pairs[(curr_jump, jump_size + 1)] = True
                rightward_shift = 0
                continue

        if index + rightward_shift == stone_count:
            return True
        else:
            return False
