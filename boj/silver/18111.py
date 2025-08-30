import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

max_height = 256 + 1
comp = [0] * max_height

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        comp[arr[i][j]] += 1

result_time = 2e19
result_height = 0

for target in range(max_height):
    time = 0
    use_block = 0
    take_block = 0
    for i in range(max_height):
        if comp[i] == 0: continue

        if target > i:
            use_block += (target - i) * comp[i]
        else:
            take_block += (i - target) * comp[i]

    time = take_block * 2 + use_block
    if b + take_block >= use_block:
        if time <= result_time:
            result_time = time
            result_height = target

print(result_time, result_height)
