import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

while q:
    cur_h, cur_n, cur_m = q.popleft()
    for i in range(6):
        next_h = cur_h + dh[i]
        next_n = cur_n + dy[i]
        next_m = cur_m + dx[i]

        if 0 <= next_h < h and 0 <= next_n < n and 0 <= next_m < m:
            if box[next_h][next_n][next_m] == 0:
                box[next_h][next_n][next_m] = box[cur_h][cur_n][cur_m] + 1
                q.append((next_h, next_n, next_m))

day = 0
found_unripe = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                found_unripe = True
                break
            day = max(day, box[i][j][k])
        if found_unripe:
            break
    if found_unripe:
        break

if found_unripe:
    print(-1)
else:
    print(day-1)
