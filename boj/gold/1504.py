import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


first_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

path_A = first_dist[v1] + v1_dist[v2] + v2_dist[N]
path_B = first_dist[v2] + v2_dist[v1] + v1_dist[N]

result = min(path_A, path_B)

if result >= INF:
    print(-1)
else:
    print(result)
