n = int(input())
dir_list = list(map(str, input().split()))

x, y = 1, 1

for dir in dir_list:
    if dir == 'R' and x < n:
        x += 1
    elif dir == 'L' and x > 1:
        x -= 1
    elif dir == 'U' and y > 1:
        y -= 1
    elif dir == 'D' and y < n:
        y += 1

print(y, x)
