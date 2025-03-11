t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    while n > 0:
        if n % 2 == 1:
            print(count, end=' ')
        count += 1
        n //= 2
    print()
