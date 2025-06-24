import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = {}
idx = 1
for _ in range(n):
    input_name = input().strip()
    arr[idx] = input_name
    idx += 1

arr_rev = {v.lower(): k for k, v in arr.items()}

for _ in range(m):
    input_q = input().strip()
    if input_q.isdigit() and 1 <= int(input_q) <= n:
        print(arr[int(input_q)])
    else:
        print(arr_rev[input_q.lower()])
