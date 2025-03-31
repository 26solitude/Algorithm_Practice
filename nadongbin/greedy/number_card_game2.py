n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

min_rows = [min(row) for row in nums]
result = max(min_rows)

print(result)
