# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# t = int(input())
#
# arr = set()
#
# for _ in range(t):
#     start, end = map(int, input().split())
#     arr.add((start, end))
#
# count = set()
#
#
# def dfs(start):
#     endList = [y for x, y in arr if x == start] + [x for x, y in arr if y == start]
#
#     if endList:
#         for i in endList:
#             if i not in count:
#                 count.add(i)
#                 dfs(i)
#
#
# count.add(1)
# dfs(1)
#
# print(len(count) - 1)


import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
t = int(input())

graph = defaultdict(list)
count = set()
count.add(1)

for _ in range(t):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if i not in count:
            count.add(i)
            q.append(i)

print(len(count) - 1)
