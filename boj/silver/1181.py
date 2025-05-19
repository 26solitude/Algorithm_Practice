import sys

input = sys.stdin.readline
t = int(input())
arr = []
for _ in range(t):
    arr.append(input())

arr = set(arr)

sorted_arr = sorted(arr, key=lambda w: (len(w), w))

res = "".join(sorted_arr)
print(res)
