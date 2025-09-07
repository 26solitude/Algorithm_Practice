import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, arr, visited):
    count = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and arr[next_x][next_y] == '1' and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                q.append((next_x, next_y))
    return count


count = 0
result = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            result.append(bfs(i, j, arr, visited))
            count += 1

print(count)
print("\n".join(str(x) for x in sorted(result)))
