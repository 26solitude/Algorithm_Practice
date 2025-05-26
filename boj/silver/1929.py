m, n = map(int, input().split())

arr = [True] * (n + 1)
arr[0], arr[1] = False, False

limit = int(n ** 0.5)
for i in range(2, limit + 1):
    if arr[i]:
        for j in range(i * i, n + 1, i):
            arr[j] = False

out = []
for i in range(m, n + 1):
    if arr[i]:
        out.append(str(i))

print("\n".join(out))
