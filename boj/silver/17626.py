# import sys
#
# n = int(sys.stdin.readline())
#
# dp = [0] * (n + 1)
#
# for i in range(1, n + 1):
#     dp[i] = dp[i - 1] + 1
#     j = 1
#     while j ** 2 <= i:
#         if dp[i] == 0:
#             dp[i] = dp[i - j ** 2] + dp[j ** 2]
#         else:
#             dp[i] = min(dp[i], dp[i - j ** 2] + dp[j ** 2])
#         j += 1
#
# print(dp[n])


import math
import sys

n = int(sys.stdin.readline())

if int(math.sqrt(n)) ** 2 == n:
    print(1)
    sys.exit()

for i in range(1, int(math.sqrt(n)) + 1):
    if int(math.sqrt(n - i ** 2)) ** 2 == n - i ** 2:
        print(2)
        sys.exit()

temp = n
while temp % 4 == 0:
    temp //= 4
if temp % 8 == 7:
    print(4)
    sys.exit()

print(3)
