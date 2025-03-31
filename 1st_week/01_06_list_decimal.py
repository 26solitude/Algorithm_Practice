input = 2024


# def find_prime_list_under_number(number):
#     ans = []
#     for i in range(2, number + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             ans.append(i)
#
#     return ans


# def find_prime_list_under_number(number):
#     num = [True] * (number + 1)
#
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if num[i]:
#             for j in range(i * i, number + 1, i):
#                 num[j] = False
#
#     ans = [x for x in range(2, number + 1) if num[x]]
#     return ans


def find_prime_list_under_number(number):
    prime = []

    for i in range(2, number + 1):
        for j in prime:
            if i % j == 0 and j * j <= number:
                break
        else:
            prime.append(i)

    return prime


result = find_prime_list_under_number(input)
print(result)
