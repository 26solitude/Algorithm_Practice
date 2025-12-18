import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input())
INF = float('inf')

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(start):
    distances = [INF] * (V + 1)
    q = []

    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for w, next_node in graph[now]:
            next_dist = dist + w
            if distances[next_node] > next_dist:
                distances[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))

    return distances


result = dijkstra(start)

output = []
for i in range(1, V + 1):
    if result[i] == INF:
        output.append("INF")
    else:
        output.append(str(result[i]))

print('\n'.join(output))
