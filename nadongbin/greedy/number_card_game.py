import heapq

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
result = []

for row_nums in nums:
    min_num = 1e9
    for num in row_nums:
        if num < min_num:
            min_num = num
    heapq.heappush(result, -min_num)

print(-heapq.heappop(result))
