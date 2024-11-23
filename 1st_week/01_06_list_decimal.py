input = 2024

# def find_prime_list_under_number(number):
#     ans = []
#     for i in range(2, number + 1):
#         decimal_check = True
#         for j in range(2, i):
#             if i % j == 0:
#                 decimal_check = False
#                 break
#         if decimal_check:
#             ans.append(i)
#
#     return ans

import math


def find_prime_list_under_number(number):
    num = [True] * (number + 1)
    num[0], num[1] = False, False

    for i in range(2, int(math.sqrt(number)) + 1):
        if num[i]:
            for j in range(i * i, number + 1, i):
                num[j] = False

    ans = [x for x in range(number + 1) if num[x]]
    return ans


result = find_prime_list_under_number(input)
print(result)
