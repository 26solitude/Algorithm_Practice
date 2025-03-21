# import itertools
#
#
# def permutations(input, n):
#     result = []
#     for i in range(4):
#         if input[i] > 0:
#             for j in range(input[i]):
#                 result.append(i)
#     return list(itertools.permutations(result, n - 1))
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# op_input = list(map(int, input().split()))
#
# MIN = 1000000000
# MAX = -1000000000
#
# op_permutation_list = permutations(op_input, n)
# for op_list in op_permutation_list:
#     num = arr[0]
#     for i in range(1, n):
#         if op_list[i - 1] == 0:
#             num += arr[i]
#         elif op_list[i - 1] == 1:
#             num -= arr[i]
#         elif op_list[i - 1] == 2:
#             num *= arr[i]
#         else:
#             num = int(num / arr[i])
#     if num > MAX:
#         MAX = num
#     if num < MIN:
#         MIN = num
#
# print(MAX)
# print(MIN)


def find_min_max(depth, total, plus, minus, multiply, divide):
    global MAX, MIN
    if depth == n:
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return

    if plus:
        find_min_max(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        find_min_max(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        find_min_max(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        find_min_max(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)


n = int(input())
nums = list(map(int, input().split()))
op_input = list(map(int, input().split()))

MAX = -1e9
MIN = 1e9

find_min_max(1, nums[0], op_input[0], op_input[1], op_input[2], op_input[3])
print(MAX)
print(MIN)
