import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    q = deque()
    visited = [False] * n

    for j in graph[i]:
        q.append(j)
        visited[j] = True
        result[i][j] = 1

    while q:
        cur = q.popleft()

        for next_idx in graph[cur]:
            if not visited[next_idx]:
                visited[next_idx] = True
                result[i][next_idx] = 1
                q.append(next_idx)

for row in result:
    print(' '.join(map(str, row)))