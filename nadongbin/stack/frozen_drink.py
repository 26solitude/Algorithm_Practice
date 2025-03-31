n, m = map(int, input().split())
ice_map = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(ice_map, x, y):
    if ice_map[x][y] == 0:
        ice_map[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(ice_map, nx, ny)


count = 0
for i in range(n):
    for j in range(m):
        if ice_map[i][j] == 0:
            count += 1
            dfs(ice_map, i, j)

print(count)
