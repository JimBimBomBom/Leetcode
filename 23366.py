result_1 = list()
result_2 = list()


def add_to_list(left_val, val, num_of_val):
    itterator = 0
    while itterator < num_of_val:
        result_2.append(val)
        itterator += 1
    result_2.append(left_val)


def decompose(min_, val, max_) -> (int, int):
    global result_1, result_2

    left_val = min_
    num_of_additions = 0
    if val <= max_:  # val is set correctly to get a non-decreasing order
        add_to_list(val, 0, 0)
        return (val, num_of_additions)

    itterator = max_
    best_minimum = 0
    best_itterator = 0
    division_was_clean = False
    while itterator >= 1:
        if best_minimum >= itterator:
            break
        remainder = val % itterator
        best_curr = 0
        if remainder == 0:
            best_curr = itterator
        else:
            best_curr = remainder
        if best_curr > best_minimum:
            if remainder == 0:
                division_was_clean = True
            else:
                division_was_clean = False
            best_minimum = best_curr
            best_itterator = itterator
        itterator -= 1

    append_num = val//best_itterator
    if division_was_clean:
        append_num -= 1
    add_to_list(best_minimum, best_itterator, append_num)
    print(min_, val, max_)
    print("Adding: ", best_minimum, '+', best_itterator, '*', append_num)
    return (best_minimum, append_num)


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        global result_1, result_2

        result = 0
        result_1 = nums.copy()
        result_2.clear()
        left_val = 0
        right_val = 0
        num_count = len(result_1)
        right_val = result_1[num_count - 1]
        index = num_count - 2
        while index >= 0:
            val = result_1[index]
            if index == 0:
                left_val = 0
            else:
                left_val = result_1[index - 1]

            decomposition_result = decompose(left_val, val, right_val)
            num_of_addends = decomposition_result[1]
            right_val = decomposition_result[0]
            result += num_of_addends
            index -= 1

        result_2.reverse()
        result_2.append(result_1[len(result_1) - 1])
        print(result_2)
        # print()
        result_1.clear()

        return result
