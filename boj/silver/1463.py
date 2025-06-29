import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
visited = [0] * (n + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        if cur == 1:
            break
        if cur % 3 == 0 and visited[cur // 3] == 0:
            visited[cur // 3] = visited[cur] + 1
            q.append(cur // 3)
        if cur % 2 == 0 and visited[cur // 2] == 0:
            visited[cur // 2] = visited[cur] + 1
            q.append(cur // 2)
        if visited[cur - 1] == 0:
            visited[cur - 1] = visited[cur] + 1
            q.append(cur - 1)


bfs()
print(visited[1])

# import sys
#
# input = sys.stdin.readline
# n = int(input())
#
# arr = [0] * (n + 1)
#
# for i in range(2, n + 1):
#     arr[i] = arr[i - 1] + 1
#
#     if i % 2 == 0:
#         arr[i] = min(arr[i], arr[i // 2] + 1)
#
#     if i % 3 == 0:
#         arr[i] = min(arr[i], arr[i // 3] + 1)
#
# print(arr[n])
