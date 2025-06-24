import sys

input = sys.stdin.readline

n, k = map(int, input().split())
result = 0
arr = []
for _ in range(n):
    arr.append(int(input().strip()))

arr.sort(reverse=True)
for i in arr:
    if k == 0:
        break
    if k >= i:
        div = k // i
        result += div
        k -= i * div

print(result)
