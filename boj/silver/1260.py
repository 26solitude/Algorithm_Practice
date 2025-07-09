# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m, v = map(int, input().split())
#
# graph = [[False] * (n + 1) for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = True
#     graph[b][a] = True
#
# visited1 = [False] * (n + 1)
# visited2 = [False] * (n + 1)
#
#
# def bfs(v):
#     q = deque([v])
#     visited1[v] = True
#     while q:
#         p = q.popleft()
#         print(p, end=" ")
#         for i in range(1, n + 1):
#             if not visited1[i] and graph[p][i]:
#                 q.append(i)
#                 visited1[i] = True
#
#
# def dfs(v):
#     visited2[v] = True
#     print(v, end=" ")
#     for i in range(1, n + 1):
#         if not visited2[i] and graph[v][i]:
#             dfs(i)
#
#
# dfs(v)
# print()
# bfs(v)


import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)
print()
