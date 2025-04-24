x = int(input())
dp = [-1] * (x + 1)


def solve(n):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]

    res = solve(n - 1) + 1
    if n % 2 == 0:
        res = min(res, solve(n // 2) + 1)
    if n % 3 == 0:
        res = min(res, solve(n // 3) + 1)
    if n % 5 == 0:
        res = min(res, solve(n // 5) + 1)

    dp[n] = res
    return dp[n]


print(solve(x))
