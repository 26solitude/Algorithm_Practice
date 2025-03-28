n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

result = 0
count = 0

for i in range(m):
    if count == k:
        result += nums[1]
        count = 0
    else:
        result += nums[0]
        count += 1

print(result)