import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]


def find_start(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j
    return -1, -1


start = find_start(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 0

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if arr[next_x][next_y] == 1 and visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    q.append((next_x, next_y))


bfs(find_start(arr))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            visited[i][j] = 0

for i in visited:
    print(' '.join(map(str, i)))
