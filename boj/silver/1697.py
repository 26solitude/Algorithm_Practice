import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 1000001
visited[n] = 0

q = deque([n])
rep = 0

while q:
    idx = q.popleft()
    if idx == k:
        print(visited[idx])
        break
    if 0 <= idx + 1 <= 100000 and visited[idx + 1] == -1:
        q.append(idx + 1)
        visited[idx + 1] = visited[idx] + 1
    if 0 <= idx - 1 <= 100000 and visited[idx - 1] == -1:
        q.append(idx - 1)
        visited[idx - 1] = visited[idx] + 1
    if 0 <= idx * 2 <= 100000 and visited[idx * 2] == -1:
        q.append(idx * 2)
        visited[idx * 2] = visited[idx] + 1
