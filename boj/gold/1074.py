import sys

N, r, c = map(int, sys.stdin.readline().split())


def solve(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)

    if r < half and c < half:
        return solve(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + solve(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + solve(n - 1, r - half, c)
    else:
        return 3 * half * half + solve(n - 1, r - half, c - half)


result = solve(N, r, c)
print(result)
