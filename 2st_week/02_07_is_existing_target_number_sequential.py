# finding_target = 14
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#
#
# def is_existing_target_number_sequential(target, array):
#     for number in array:
#         if target == number:
#             return True
#     return False
#
#
# result = is_existing_target_number_sequential(finding_target, finding_numbers)
# print(result)  # True

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        now_index = (min_index + max_index) // 2
        if array[now_index] == target:
            return True
        elif array[now_index] < target:
            min_index = now_index + 1
        elif array[now_index] > target:
            max_index = now_index - 1


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
