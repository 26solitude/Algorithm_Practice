import sys
from collections import deque

input = sys.stdin.readline

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def find_start(n, m, campus):
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                return i, j
    return -1, -1


def bfs(n, m, campus, start_pos):
    q = deque([start_pos])
    visited = [[False] * m for _ in range(n)]

    next_x, next_y = start_pos
    visited[next_x][next_y] = True

    person_count = 0

    while q:
        cur_x, cur_y = q.popleft()

        if campus[cur_x][cur_y] == 'P':
            person_count += 1

        for i in range(4):
            next_x, next_y = cur_x + DX[i], cur_y + DY[i]
            if not (0 <= next_x < n and 0 <= next_y < m):
                continue
            if visited[next_x][next_y] or campus[next_x][next_y] == 'X':
                continue

            visited[next_x][next_y] = True
            q.append((next_x, next_y))

    return person_count


def solution():
    n, m = map(int, input().split())
    campus = [list(input().strip()) for _ in range(n)]
    start_pos = find_start(n, m, campus)
    result = bfs(n, m, campus, start_pos)
    if result == 0:
        print("TT")
    else:
        print(result)


solution()
