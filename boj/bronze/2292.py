n = int(input())
i = 1
sum = 1
add = 0
while True:
    if sum >= n:
        break
    add += 6
    sum += add
    i += 1

print(i)