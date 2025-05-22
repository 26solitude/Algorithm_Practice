import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    age, name = (lambda a, n: (int(a), n))(*input().split())
    arr.append((age, name))

sorted_arr = sorted(arr, key=lambda x: x[0])

# for age, name in sorted_arr:
#     print(age, name)
print('\n'.join(f"{age} {name}" for age, name in sorted_arr))
