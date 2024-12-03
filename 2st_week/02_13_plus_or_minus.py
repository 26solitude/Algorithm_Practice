# def solution(array, target):
#     def make_number_of_cases(index, current_case):
#         if index == len(array):
#             return [current_case]
#
#         plus_case = make_number_of_cases(index + 1, current_case + [array[index]])
#         minus_case = make_number_of_cases(index + 1, current_case + [-array[index]])
#
#         return plus_case + minus_case
#
#     all_cases = make_number_of_cases(0, [])
#     count = 0
#     for case in all_cases:
#         sum = 0
#         for num in case:
#             sum += num
#         if sum == target:
#             count += 1
#     return count

# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


def solution(numbers, target):
    res = []

    def make_all_cases(numbers, sum, index):
        if index == len(numbers):
            res.append(sum)
            return
        make_all_cases(numbers, sum + numbers[index], index + 1)
        make_all_cases(numbers, sum - numbers[index], index + 1)

    make_all_cases(numbers, 0, 0)

    count = 0
    for case in res:
        if case == target:
            count += 1

    return count


print(solution([1, 1, 1, 1, 1], 3))
