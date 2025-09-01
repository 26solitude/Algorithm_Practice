import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

window_counts = {}
start = 0
result = 0

for end in range(n):
    end_num = arr[end]

    window_counts[end_num] = window_counts.get(end_num, 0) + 1

    while len(window_counts) > 2:
        start_num = arr[start]
        window_counts[start_num] -= 1

        if window_counts[start_num] == 0:
            del window_counts[start_num]

        start += 1

    current_length = end - start + 1

    result = max(result, current_length)

print(result)
