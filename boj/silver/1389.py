import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
kevin_graph = [[2e19] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(i, graph):
    q = deque([i])
    distance = [-1] * (n + 1)
    distance[i] = 0

    while q:
        cur_idx = q.popleft()
        for neighbor in graph[cur_idx]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[cur_idx] + 1
                q.append(neighbor)

    return sum(d for d in distance if d > 0)


result = 2e19
result_idx = 0

for i in range(1, n + 1):
    value = bfs(i, graph)
    if value < result:
        result = value
        result_idx = i

print(result_idx)
