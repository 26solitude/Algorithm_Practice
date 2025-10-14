import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

parent = [0] * (n + 1)
visited = [False for _ in range(n + 1)]

q = deque([1])
while q:
    cur_node = q.popleft()
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = cur_node
            q.append(next_node)

for i in range(2, n + 1):
    print(parent[i])
