def to_one(n, k, rep):
    global MIN
    if n == 1:
        MIN = min(MIN, rep)
        return

    if n % k == 0:
        to_one(n // k, k, rep + 1)
    to_one(n - 1, k, rep + 1)


n, k = map(int, input().split())
MIN = 1e9
to_one(n, k, 0)
print(MIN)