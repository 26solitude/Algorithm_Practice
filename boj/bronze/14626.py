arr = list(input())
arr_sum = sum(int(x) if i % 2 == 0 else (int(x) * 3) for i, x in enumerate(arr) if x != '*') % 10
target_idx = 1 if arr.index('*') % 2 == 0 else 3
result = 0
for i in range(1, 10):
    if (target_idx * i + arr_sum) % 10 == 0:
        result = i
        break

print(result)