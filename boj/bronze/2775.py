t = int(input())

MAX = 14

dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for i in range(MAX + 1):
    dp[0][i] = i

for i in range(1, MAX + 1):
    dp[i][1] = 1
    for j in range(2, MAX + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]


def people(k, n):
    return dp[k][n]


for i in range(t):
    k = int(input())
    n = int(input())
    print(people(k, n))