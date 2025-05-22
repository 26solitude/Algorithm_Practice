import sys

input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

rank = []

for x, y in arr:
    rank.append(sum([1 for c_x, c_y in arr if c_x > x and c_y > y]) + 1)

print(" ".join(map(str, rank)))
