import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())


def dijkstra(start):
    q = []

    distances = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distances[end]


print(dijkstra(start))
