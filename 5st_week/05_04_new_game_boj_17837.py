dr = [0, 1, -1, 0, 0]
dc = [0, 0, 0, 1, -1]


def change_dir(d):
    if d % 2 == 0:
        return d - 1
    else:
        return d + 1


def new_game(N, K, chess_map, horses):
    horse_map = [[[] for i in range(N)] for i in range(N)]
    for i in range(K):
        x, y, d = horses[i]
        x -= 1
        y -= 1
        horse_map[x][y].append(i)
        horses[i] = x, y, d

    count = 0
    while True:
        if count >= 1000: return -1
        count += 1

        for i in range(K):
            x, y, d = horses[i]
            dx = x + dr[d]
            dy = y + dc[d]
            if 0 <= dx < N and 0 <= dy < N:
                if chess_map[dx][dy] == 0:
                    while horse_map[x][y]:
                        horse_map[dx][dy].append(horse_map[x][y].pop())
                        horses[i] = dx, dy, d
                elif chess_map[dx][dy] == 1:
                    while horse_map[x][y]:
                        horse_map[dx][dy].append(horse_map[x][y].pop())
                        horses[i] = dx, dy, d
                else:
                    d = change_dir(d)
                    dx = x + dr[d]
                    dy = y + dc[d]
                    if 0 <= dx < N and 0 <= dy < N:
                        if chess_map[dx][dy] == 0:
                            while horse_map[x][y]:
                                horse_map[dx][dy].append(horse_map[x][y].pop())
                            horses[i] = dx, dy, d
                        elif chess_map[dx][dy] == 1:
                            while horse_map[x][y]:
                                horse_map[dx][dy].append(horse_map[x][y].pop())
                            horses[i] = dx, dy, d
            if 0 <= dx < N and 0 <= dy < N and len(horse_map[dx][dy]) >= 4:
                return count


N, K = map(int, input().split())
chess_map = [list(map(int, input().split())) for _ in range(N)]
horses = [list(map(int, input().split())) for _ in range(K)]

print(new_game(N, K, chess_map, horses))
