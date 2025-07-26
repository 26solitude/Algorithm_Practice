# from queue import PriorityQueue
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# q = PriorityQueue()
#
# for _ in range(n):
#     x = int(input())
#     if x == 0:
#         if q.empty():
#             print(0)
#         else:
#             print(q.get())
#     else:
#         q.put(x)

import heapq
import sys

input = sys.stdin.readline

q = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)
