import math

n = int(input())
m = int(input())

rep = int(math.sqrt(m)) + 1

arr = list(range(0, m + 1))
arr[0] = 0
arr[1] = 0

for i in range(2, rep):
    for j in range(i * i, m + 1, i):
        arr[j] = 0
res = []
for i in range(n, m + 1):
    if arr[i] != 0:
        res.append(arr[i])

res.sort()
if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)
