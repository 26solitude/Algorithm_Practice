n, k = map(int, input().split())
a = 1
for i in range(1, n + 1):
    a *= i
b = 1
c = 1
for j in range(1, k + 1):
    b *= j
for k in range(1, n - k + 1):
    c *= k

print(int(a / (b * c)))
