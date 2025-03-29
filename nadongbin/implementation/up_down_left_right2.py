n = int(input())
dir_arr = input().split()

moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
x, y = 1, 1

for direction in dir_arr:
    dx, dy = moves.get(direction, (0, 0))
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)
