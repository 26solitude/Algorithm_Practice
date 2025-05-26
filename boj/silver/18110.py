import sys

input = sys.stdin.readline
n = int(input())
if n == 0:
    res = 0
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    av = int(n * 0.15 + 0.5)

    total = sum(arr)
    head = sum(arr[:av])
    tail = sum(arr[n-av:])

    res = int((total - (head + tail)) / (n - 2 * av) + 0.5)

print(res)
