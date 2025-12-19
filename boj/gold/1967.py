# import heapq
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(n-1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))
#
# INF = float('inf')
#
#
# def dijkstra(start):
#     distances = [INF] * (n + 1)
#     distances[start] = 0
#
#     q = []
#     heapq.heappush(q, (0, start))
#
#     while q:
#         dist, now = heapq.heappop(q)
#         if distances[now] < dist:
#             continue
#
#         for next_node, next_dist in graph[now]:
#             next_dist += dist
#             if distances[next_node] > next_dist:
#                 distances[next_node] = next_dist
#                 heapq.heappush(q, (next_dist, next_node))
#
#     return distances
#
# def find_max(arr):
#     max_val = 0
#     for i in arr:
#         if i != INF and max_val < i:
#             max_val = i
#     return max_val
#
# one = dijkstra(1)
# max_val = find_max(one)
# max_idx = one.index(max_val)
# two = dijkstra(max_idx)
# result = find_max(two)
# print(result)


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v, w, u = map(int, input().split())
    graph[v].append((w, u))
    graph[w].append((v, u))


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1] * (n + 1)
    visited[start] = 0

    max_dist_info = (0, start)

    while q:
        now = q.popleft()

        for next_node, weight in graph[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + weight
                q.append(next_node)

                if visited[next_node] > max_dist_info[0]:
                    max_dist_info = (visited[next_node], next_node)

    return max_dist_info


dist1, node_a = bfs(1)
final_dist, node_b = bfs(node_a)

print(final_dist)
