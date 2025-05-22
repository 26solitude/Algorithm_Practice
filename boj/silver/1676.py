n = int(input())
fac = 1
for i in range(2, n+1):
    fac *= i

cnt = 0
while fac:
    num = fac % 10
    if num != 0:
        break
    cnt += 1
    fac //= 10

print(cnt)