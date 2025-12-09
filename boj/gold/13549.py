import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001
visited[n] = 0
time = 0

q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        break

    if now * 2 < 100001 and visited[now * 2] == -1:
        visited[now * 2] = visited[now]
        q.appendleft(now * 2)

    if 0 <= now - 1 and visited[now - 1] == -1:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)

    if now + 1 < 100001 and visited[now + 1] == -1:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)

print(visited[k])
