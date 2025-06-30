# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# res = [0] * n
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# q = deque()
# q.append((0, False))
# res[0] = arr[0]
#
# while q:
#     idx, seq = q.popleft()
#     if not seq and idx + 1 < n:
#         res[idx + 1] = max(res[idx + 1], res[idx] + arr[idx + 1])
#         q.append((idx + 1, True))
#
#     if idx + 2 < n:
#         res[idx + 2] = max(res[idx + 2], res[idx] + arr[idx + 2])
#         q.append((idx + 2, False))
#
# print(res[n - 1])


import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

dp = [0] * (n + 1)
dp[1] = arr[1]

if n > 1:
    dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[n])
