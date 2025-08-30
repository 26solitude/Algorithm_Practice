import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_sorted = sorted(list(set(arr)))
coord_map = {}

for idx, value in enumerate(arr_sorted):
    coord_map[value] = idx

res = []

for i in arr:
    res.append(str(coord_map[i]))

print(' '.join(res))
