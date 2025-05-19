# n = int(input())
# arr = list(map(int, input().split()))
# t, p = map(int, input().split())
#
# ans1 = 0
# for t_shirt in arr:
#     if t_shirt % t == 0:
#         ans1 += t_shirt // t
#     else:
#         ans1 += t_shirt // t + 1
#
# ans2 = 0
# ans3 = 0
# if n % p == 0:
#     ans2 = n // p
#     ans3 = 0
# else:
#     ans2 += n // p
#     ans3 += n % p
#
# print(ans1)
# print(ans2, ans3)


import sys

input = sys.stdin.readline

n = int(input())
tshirts = map(int, input().split())
t, p = map(int, input().split())

total_boxes = sum((s + t - 1) // t for s in tshirts)
full_groups, remainder = divmod(n, p)

print(total_boxes)
print(full_groups, remainder)
