import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = []
result.append(str(round(sum(arr) / n)))

arr.sort()
result.append(str(arr[n // 2]))

cnt = Counter(arr)
max_v = max(cnt.values())
max_arr = [k for k, v in cnt.items() if v == max_v]
if len(max_arr) == 1:
    result.append(str(max_arr[0]))
else:
    result.append(str(max_arr[1]))

result.append(str(max(arr) - min(arr)))

print("\n".join(result))
