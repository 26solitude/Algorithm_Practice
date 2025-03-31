from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(maze, x, y):
    queue = deque([(x, y, 1)])

    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        maze[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny, count + 1))
    return -1


print(bfs(maze, 0, 0))
