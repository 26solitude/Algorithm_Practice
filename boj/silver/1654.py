import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

min = 1
max = max(arr)

while min <= max:
    mid = (min + max) // 2
    count = sum(x // mid for x in arr)

    if count >= n:
        result = mid
        min = mid + 1
    else:
        max = mid - 1

print(result)
