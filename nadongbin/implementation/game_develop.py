def change_dir(d):
    if d == 0:
        return 3
    else:
        return d - 1


n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(m)]
move_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
move_change = 0

game_map[x][y] = 2
count = 1

while True:
    d = change_dir(d)
    dx, dy = x + move_dir[d][0], y + move_dir[d][1]
    if game_map[dx][dy] == 0:
        game_map[dx][dy] = 2
        x, y = dx, dy
        count += 1
        move_change = 0
    else:
        move_change += 1

    if move_change == 4:
        dd = (d + 2) % 4
        dx, dy = x + move_dir[dd][0], y + move_dir[dd][1]
        if game_map[dx][dy] != 1:
            x, y = dx, dy
            move_change = 0
        else:
            break

print(count)
