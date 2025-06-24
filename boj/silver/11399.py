import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = arr[i]
    else:
        dp[i] = dp[i-1] + arr[i]

print(sum(dp))