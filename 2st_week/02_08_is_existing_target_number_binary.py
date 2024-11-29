finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, array):
    min_index = 0
    max_index = len(array) - 1

    sorted_array = sorted(array)
    print(sorted_array)

    while min_index <= max_index:
        cur_index = (min_index + max_index) // 2
        if sorted_array[cur_index] == target:
            return True
        elif sorted_array[cur_index] < target:
            min_index = cur_index + 1
        else:
            max_index = cur_index - 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
