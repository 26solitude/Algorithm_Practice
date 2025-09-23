import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

while q:
    cur_n, cur_m = q.popleft()
    for i in range(4):
        next_n, next_m = cur_n + dx[i], cur_m + dy[i]
        if 0 <= next_n < n and 0 <= next_m < m and box[next_n][next_m] == 0:
            box[next_n][next_m] = box[cur_n][cur_m] + 1
            q.append((next_n, next_m))

day = 0
find_unripe = False
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            find_unripe = True
            break
        day = max(day, box[i][j])
    if find_unripe:
        break

if find_unripe:
    print(-1)
else:
    print(day - 1)
