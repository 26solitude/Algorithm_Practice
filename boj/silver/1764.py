import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
for _ in range(n):
    name = input().strip()
    arr.add(name)

cnt = 0
res = []
for _ in range(m):
    name = input().strip()
    if name in arr:
        res.append(name)
        cnt += 1

res.sort()
print(cnt)
print("\n".join(res))