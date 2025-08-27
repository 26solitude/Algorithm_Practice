import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
count = 0


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
