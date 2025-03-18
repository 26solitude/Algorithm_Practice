n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i < 2:
        continue

    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        count += 1

print(count)
