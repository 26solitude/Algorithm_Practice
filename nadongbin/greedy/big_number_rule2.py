n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)

result = 0

result += (m // (k + 1)) * (nums[0] * k + nums[1])
result += (m % (k + 1)) * nums[0]

print(result)
