import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = {}
    for _ in range(n):
        name, tag = input().split()
        if tag in arr:
            arr[tag] += 1
        else:
            arr[tag] = 1
    res = 1
    for i in arr.values():
        res *= (i + 1)
    print(res - 1)
