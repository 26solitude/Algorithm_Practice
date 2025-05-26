import sys

input = sys.stdin.readline

n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))

result = '\n'.join(f"{x} {y}" for x, y in arr)
print(result)
