import sys

input = sys.stdin.readline

n = int(input())

home = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for r in range(0, n):
    for c in range(0, n):
        if r < 1 and c <= 1: continue
        if home[r][c] == 1: continue

        if c - 1 >= 0:
              dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]

        if r-1>=0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]

        if r-1>=0 and c-1>=0:
            if home[r-1][c] != 1 and home[r][c-1] != 1:
                dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[n-1][n-1]))