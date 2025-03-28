n, k = map(int, input().split())
result = 0

if k == 1:
    result = n - 1
else:
    while n >= k:
        remainder = n % k
        if remainder:
            result += remainder
            n -= remainder

        n = n // k
        result += 1
    result += n - 1

print(result)
